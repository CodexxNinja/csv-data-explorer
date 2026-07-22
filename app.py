from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # non-interactive backend, required for running on a server (no display)
import matplotlib.pyplot as plt
import seaborn as sns
import os
import uuid
import io
import base64

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB upload limit

ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def generate_charts(df, session_id):
    """Generate charts in memory and return them as base64-encoded strings — no files saved to disk."""
    chart_files = []
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    meaningful_cols = []
    for col in numeric_cols:
        if df[col].nunique() <= 1:
            continue
        unique_ratio = df[col].nunique() / len(df)
        if unique_ratio > 0.95 and df[col].nunique() > 50:
            continue
        meaningful_cols.append(col)

    meaningful_cols = sorted(
        meaningful_cols,
        key=lambda c: df[c].std() if df[c].std() == df[c].std() else 0,
        reverse=True
    )

    sns.set_style('darkgrid')

    def fig_to_base64():
        """Save the current matplotlib figure to an in-memory buffer and return a base64 string."""
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        plt.close()
        buf.seek(0)
        encoded = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()
        return f"data:image/png;base64,{encoded}"

    if len(meaningful_cols) >= 2:
        plt.figure(figsize=(8, 6))
        corr = df[meaningful_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        chart_files.append({'title': 'Correlation Heatmap', 'image': fig_to_base64()})

    for col in meaningful_cols[:4]:
        plt.figure(figsize=(6, 4))
        skew = df[col].skew()
        data = df[col].dropna()
        if abs(skew) > 2 and (data > 0).all():
            sns.histplot(data, kde=True, color='#6366f1', log_scale=True)
            plt.title(f'Distribution of {col} (log scale)')
        else:
            sns.histplot(data, kde=True, color='#6366f1')
            plt.title(f'Distribution of {col}')
        plt.tight_layout()
        chart_files.append({'title': f'Distribution: {col}', 'image': fig_to_base64()})

    return chart_files


def analyze_dataframe(df):
    """Build a summary report dictionary from the dataframe."""
    summary = {
        'rows': df.shape[0],
        'columns': df.shape[1],
        'column_info': [],
        'missing_values': [],
        'duplicate_rows': int(df.duplicated().sum())
    }

    for col in df.columns:
        dtype = str(df[col].dtype)
        missing_count = int(df[col].isnull().sum())
        missing_pct = round((missing_count / len(df)) * 100, 1) if len(df) > 0 else 0

        summary['column_info'].append({
            'name': col,
            'dtype': dtype,
            'unique_values': int(df[col].nunique())
        })

        if missing_count > 0:
            summary['missing_values'].append({
                'name': col,
                'count': missing_count,
                'percent': missing_pct
            })

    # Numeric summary stats (describe)
    numeric_df = df.select_dtypes(include='number')
    if not numeric_df.empty:
        desc = numeric_df.describe().round(2)
        summary['numeric_stats'] = desc.to_dict()
    else:
        summary['numeric_stats'] = None

    return summary


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected.', 'error')
            return redirect(url_for('upload'))

        file = request.files['file']

        if file.filename == '':
            flash('No file selected.', 'error')
            return redirect(url_for('upload'))

        if not allowed_file(file.filename):
            flash('Please upload a valid .csv file.', 'error')
            return redirect(url_for('upload'))

        try:
            filename = secure_filename(file.filename)
            session_id = str(uuid.uuid4())[:8]
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], f'{session_id}_{filename}')
            file.save(filepath)

            df = pd.read_csv(filepath)
            os.remove(filepath)  

            if df.empty:
                flash('The uploaded CSV appears to be empty.', 'error')
                return redirect(url_for('upload'))

            summary = analyze_dataframe(df)
            charts = generate_charts(df, session_id)

            preview_data = df.head(10).to_html(classes='preview-table', index=False, border=0)

            return render_template(
                'report.html',
                summary=summary,
                charts=charts,
                filename=filename,
                preview_data=preview_data
            )

        except Exception as e:
            flash(f'Error processing file: {str(e)}', 'error')
            return redirect(url_for('upload'))

    return render_template('upload.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)