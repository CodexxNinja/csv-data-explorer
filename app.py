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
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
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


def generate_insights(df, summary):
    """Generate plain-English insights about the dataset automatically."""
    insights = []
    numeric_df = df.select_dtypes(include='number')

    # Missing data insight
    if summary['missing_values']:
        worst = max(summary['missing_values'], key=lambda x: x['percent'])
        insights.append(f"'{worst['name']}' has the most missing data — {worst['percent']}% of its values are empty.")
    else:
        insights.append("No missing values detected — this dataset is complete.")

    # Duplicate rows insight
    if summary['duplicate_rows'] > 0:
        pct = round((summary['duplicate_rows'] / summary['rows']) * 100, 1)
        insights.append(f"Found {summary['duplicate_rows']} duplicate rows ({pct}% of the dataset) — consider removing them before analysis.")

    # Correlation insight
    if numeric_df.shape[1] >= 2:
        corr = numeric_df.corr().abs()
        # Zero out the diagonal so a column isn't "correlated with itself"
        for col in corr.columns:
            corr.loc[col, col] = 0
        max_corr = corr.max().max()
        if max_corr > 0.01:
            col1, col2 = corr.stack().idxmax()
            strength = "very strongly" if max_corr > 0.8 else "strongly" if max_corr > 0.6 else "moderately"
            insights.append(f"'{col1}' and '{col2}' are {strength} correlated (score: {round(max_corr, 2)}).")

    # Skewness insight
    skewed_cols = []
    for col in numeric_df.columns:
        skew = numeric_df[col].skew()
        if abs(skew) > 2:
            skewed_cols.append(col)
    if skewed_cols:
        cols_str = ", ".join(f"'{c}'" for c in skewed_cols[:3])
        insights.append(f"{cols_str} {'is' if len(skewed_cols) == 1 else 'are'} heavily skewed — a few extreme values are pulling the average away from the typical value.")

    # Column type balance
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    if len(cat_cols) > 0 and len(numeric_df.columns) > 0:
        insights.append(f"This dataset has {len(numeric_df.columns)} numeric column(s) and {len(cat_cols)} categorical/text column(s).")

    return insights

def detect_outliers(df):
    """Detect outliers per numeric column using the IQR method."""
    numeric_df = df.select_dtypes(include='number')
    outlier_report = []

    for col in numeric_df.columns:
        data = numeric_df[col].dropna()
        if len(data) < 4:
            continue

        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = data[(data < lower_bound) | (data > upper_bound)]
        if len(outliers) > 0:
            outlier_report.append({
                'column': col,
                'count': len(outliers),
                'percent': round((len(outliers) / len(data)) * 100, 1)
            })

    return sorted(outlier_report, key=lambda x: x['count'], reverse=True)


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
            insights = generate_insights(df, summary)
            outliers = detect_outliers(df)
            charts = generate_charts(df, session_id)

            preview_data = df.head(10).to_html(classes='preview-table', index=False, border=0)

            return render_template(
                'report.html',
                summary=summary,
                charts=charts,
                filename=filename,
                preview_data=preview_data,
                insights=insights,
                outliers=outliers
            )

        except Exception as e:
            flash(f'Error processing file: {str(e)}', 'error')
            return redirect(url_for('upload'))

    return render_template('upload.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)