# CSV Data Explorer

<img src="https://user-images.githubusercontent.com/74038190/212750342-3d7c7b2d-f0a8-43b7-b2c9-6d3b0b6d4d63.gif" width="700"/>

### Intelligent CSV Analysis using Flask, Pandas & Data Visualization

Automatically transform any uploaded CSV into a complete analytical
report with statistics, visualizations, smart insights, and outlier
detection.

<br>

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas"/>
<img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge"/>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>


------------------------------------------------------------------------

## Overview

CSV Data Explorer is a Flask web application that converts any uploaded
CSV file into an interactive analytical report. It automatically
performs dataset profiling, missing value analysis, correlation
analysis, distribution visualization, outlier detection, and generates
readable statistical insights.

Built as **Week 3** of my **Python → Flask → AI/ML Roadmap**.

------------------------------------------------------------------------

## Live Demo

> Add deployment URL after hosting.

------------------------------------------------------------------------

## Features

  Feature                Description
  ---------------------- ---------------------------------------------
  Drag & Drop Upload     Modern CSV upload interface
  Summary Statistics     Rows, columns, datatypes, unique values
  Missing Value Report   Column-wise missing data analysis
  Correlation Heatmap    Automatic numeric correlation visualization
  Distribution Charts    Intelligent chart generation
  Smart Insights         Rule-based statistical observations
  Outlier Detection      IQR-based anomaly detection
  Data Preview           First 10 rows displayed
  Secure Processing      Uploaded files removed immediately

------------------------------------------------------------------------

## Tech Stack

  Layer             Technology
  ----------------- -------------------------
  Backend           Python, Flask
  Data Processing   Pandas
  Visualization     Matplotlib, Seaborn
  Frontend          HTML5, CSS3, JavaScript
  Templates         Jinja2

------------------------------------------------------------------------

## Application Workflow

``` text
CSV Upload
    │
    ▼
Flask Backend
    │
    ▼
Pandas Data Analysis
    ├── Summary Statistics
    ├── Missing Values
    ├── Duplicate Detection
    ├── Correlation Matrix
    ├── Distribution Charts
    ├── Outlier Detection
    └── Smart Insights
    │
    ▼
Interactive HTML Report
```

------------------------------------------------------------------------

## Project Structure

``` text
csv-data-explorer/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── uploads/
├── static/
│   ├── css/
│   └── js/
└── templates/
    ├── base.html
    ├── upload.html
    └── report.html
```

------------------------------------------------------------------------

## Local Setup

``` bash
git clone https://github.com/CodexxNinja/csv-data-explorer.git
cd csv-data-explorer

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
```

Create `.env`

``` env
SECRET_KEY=your_generated_secret_key
```

Run

``` bash
python app.py
```

Open:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## What the Application Analyzes

-   Dataset dimensions
-   Column data types
-   Missing values
-   Duplicate rows
-   Summary statistics
-   Correlation matrix
-   Distribution plots
-   Outlier detection using IQR
-   Smart statistical observations
-   Data preview

------------------------------------------------------------------------

## License

This project is open source and available for learning purposes.
