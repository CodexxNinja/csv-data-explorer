# 📊 CSV Data Explorer

A Flask web app that turns any uploaded CSV into an instant data report — summary statistics, missing value detection, correlation heatmaps, and distribution charts — without writing a single line of analysis code yourself.

Built as **Week 3** of my Python → Flask → AI/ML project roadmap.

---

## 🚀 Live Demo

🔗 [Live App](#) *(add link after deploying)*

---

## ✨ Features

- 📁 **Drag & Drop CSV Upload** — with a polished custom UI
- 📈 **Automatic Summary Statistics** — row/column counts, data types, unique value counts
- ⚠️ **Missing Value Report** — visual breakdown of which columns have missing data and how much
- 🔥 **Correlation Heatmap** — auto-generated with Seaborn, showing relationships between numeric columns
- 📊 **Smart Distribution Charts** — automatically skips constant/ID-like columns and uses log scale for heavily skewed data (like income), so charts stay meaningful even on messy real-world datasets
- 🧾 **Data Preview Table** — first 10 rows rendered directly from the uploaded file
- 🤖 **Smart Insights** — automated plain-English observations about the dataset (strongest correlation, most missing data, skewed columns, duplicate rows) generated through statistical reasoning, not hardcoded text
- 🎯 **Outlier Detection** — automatically flags unusual values in each numeric column using the IQR (Interquartile Range) method
- 🗑️ **Zero Storage Footprint** — charts are generated in-memory and embedded directly as images; uploaded files are deleted immediately after processing, so nothing accumulates on the server

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Data Analysis | Pandas |
| Visualization | Matplotlib, Seaborn |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Templating | Jinja2 |

---

## ⚙️ How It Works

1. A user uploads a CSV via drag-and-drop or file browser.
2. Flask reads it into a Pandas DataFrame and immediately deletes the temporary uploaded file — nothing is kept on disk.
3. The app analyzes the DataFrame: row/column counts, data types, missing values, duplicate rows, and numeric summary statistics.
4. For visualizations, the app filters out columns that aren't meaningful to plot (completely constant values, or ID-like columns with too many unique values), then prioritizes columns with the most variance.
5. Charts are rendered with Matplotlib/Seaborn directly into an in-memory buffer, base64-encoded, and embedded straight into the HTML — no image files are ever saved to disk.
6. A rule-based insight engine scans the statistical summary and generates plain-English observations — e.g. flagging the most correlated column pair, the column with the most missing data, or heavily skewed distributions.
7. Each numeric column is scanned for outliers using the IQR method (values falling outside 1.5× the interquartile range), and flagged columns are shown in a dedicated table.
8. The full report — stats, insights, missing values, outliers, charts, and a data preview — is rendered on one page.

---

## 📂 Project Structure

```
csv-data-explorer/
├── app.py                  # Flask routes, Pandas analysis, chart generation
├── requirements.txt
├── .env
├── .gitignore
├── uploads/                 # temporary storage, files deleted immediately after reading
├── static/
│   ├── css/style.css
│   └── js/script.js         # drag-and-drop UX
└── templates/
    ├── base.html
    ├── upload.html
    └── report.html
```

---

## 💻 Running Locally

### 1. Clone and set up
```bash
git clone https://github.com/CodexxNinja/csv-data-explorer.git
cd csv-data-explorer
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
```

### 2. Add environment variables
Create a `.env` file:
```
SECRET_KEY=your_generated_secret_key
```

### 3. Run
```bash
python app.py
```
Visit `http://127.0.0.1:5000`, upload any CSV file, and view the generated report.

---

## 🧠 What I Learned Building This

- Using Pandas to profile a dataset automatically: dtypes, missing values, duplicates, and descriptive statistics
- Generating Matplotlib/Seaborn charts on a server with no display (`Agg` backend) and converting them to base64 images instead of saving files — a stateless approach that works on any hosting platform without leaving files behind
- Writing chart-selection logic that adapts to the actual dataset instead of blindly plotting the first few columns — skipping constant/ID-like columns and using log scale for skewed data
- Building a rule-based insight engine that turns raw statistics (correlation, skewness, missing data) into readable, human-friendly observations
- Implementing outlier detection using the IQR statistical method
- Debugging a subtle HTML/browser quirk where a `hidden` + `required` file input silently blocks form submission
- Handling file uploads safely in Flask, including size limits and cleanup

---

## 🗺️ What's Next

Week 4 moves into Numpy — building an image processing tool using raw array manipulation.

---

## 📄 License

This project is open source and available for anyone to learn from.
