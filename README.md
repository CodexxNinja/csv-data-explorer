<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/216656977-ef584e23-480a-4d1f-8c3f-0f8d2b5b5f6b.gif" width="100%">

# CSV Data Explorer

### Turn Any CSV Into an Interactive Data Report

<p>
A modern Flask web application that instantly transforms uploaded CSV files into detailed analytical reports featuring descriptive statistics, missing value analysis, smart insights, correlation heatmaps, distribution charts, outlier detection, and interactive visualizations — all without writing a single line of analysis code.
</p>

<img src="https://user-images.githubusercontent.com/74038190/216656965-39a36c9d-8db8-4a7e-9b8b-d59c79e5b8d3.gif" width="450">

</div>

---

<div align="center">

## Project Status

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Flask-Web%20Application-000000?style=for-the-badge&logo=flask">
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas">
<img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge">
<img src="https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge">
<img src="https://img.shields.io/badge/HTML5-CSS3-JavaScript?style=for-the-badge&logo=html5">
<img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge">

</div>

---

<div align="center">

## Live Demo

[![Live App](https://img.shields.io/badge/Live_Demo-Online-brightgreen?style=for-the-badge)](https://csv-data-explorer-8dkj.onrender.com)

---

<div align="center">

## Project Overview

</div>

**CSV Data Explorer** is designed to eliminate the repetitive work involved in exploring datasets. Instead of manually inspecting data, writing analysis scripts, and generating plots, users simply **upload a CSV file and receive a comprehensive report within seconds.**

The application automatically **profiles the dataset**, computes descriptive statistics, detects missing values and duplicate records, identifies outliers, generates meaningful visualizations, and produces plain-English insights based entirely on statistical analysis.

Unlike many simple CSV viewers, this project intelligently skips columns that don't provide meaningful visualizations, detects heavily skewed data, applies logarithmic scaling where appropriate, and generates charts completely in memory without storing files on the server.

---

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212744275-c56d4d31-f9b3-4b8d-a67b-fb70b2f9d8d3.gif" width="70">

# Features

</div>

<table>
<tr>
<td width="50%">

### Smart CSV Upload

Upload datasets through an elegant drag-and-drop interface or browse directly from your system.

</td>

<td width="50%">

### Automatic Dataset Profiling

Instantly generates row counts, column counts, data types, unique values, and descriptive statistics.

</td>
</tr>

<tr>
<td>

### Missing Value Analysis

Highlights incomplete data with percentage calculations and visual summaries.

</td>

<td>

### Correlation Heatmaps

Automatically creates correlation matrices for numeric columns using Seaborn.

</td>
</tr>

<tr>
<td>

### Intelligent Distribution Charts

Skips constant and ID-like columns while selecting the most meaningful features for visualization.

</td>

<td>

### Smart Scaling

Automatically applies logarithmic scaling to highly skewed numerical distributions.

</td>
</tr>

<tr>
<td>

### Interactive Data Preview

Displays the first rows of the uploaded dataset for quick inspection.

</td>

<td>

### Rule-Based Insights

Produces human-readable observations about correlations, missing data, duplicates, skewness, and overall dataset quality.

</td>
</tr>

<tr>
<td>

### Outlier Detection

Detects unusual observations using the Interquartile Range (IQR) statistical method.

</td>

<td>

### Zero Storage Design

Uploaded files are removed immediately after processing while charts are generated entirely in memory.

</td>
</tr>
</table>

---

<div align="center">

## Why This Project?

</div>

Traditional CSV viewers only display raw tables. This application goes several steps further by automatically understanding the uploaded dataset and presenting meaningful statistical information that helps users begin exploratory data analysis immediately.

Whether the uploaded file contains customer information, sales records, survey responses, financial transactions, or machine learning datasets, the application adapts its analysis automatically and generates relevant visual reports without requiring any programming knowledge.

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212744289-38d25f79-2b2f-4a70-a2f5-c87dfc3e59d1.gif" width="100%">

</div>
<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212744275-c56d4d31-f9b3-4b8d-a67b-fb70b2f9d8d3.gif" width="70">

# Tech Stack

</div>

<div align="center">

<table>
<tr>

<td align="center" width="20%">
<img src="https://skillicons.dev/icons?i=python" width="65"><br>
<b>Python</b>
</td>

<td align="center" width="20%">
<img src="https://skillicons.dev/icons?i=flask" width="65"><br>
<b>Flask</b>
</td>

<td align="center" width="20%">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="65"><br>
<b>Pandas</b>
</td>

<td align="center" width="20%">
<img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" width="65"><br>
<b>Matplotlib</b>
</td>

<td align="center" width="20%">
<img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" width="65"><br>
<b>Seaborn</b>
</td>

</tr>

<tr>

<td align="center">
<img src="https://skillicons.dev/icons?i=html" width="65"><br>
<b>HTML5</b>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=css" width="65"><br>
<b>CSS3</b>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=javascript" width="65"><br>
<b>JavaScript</b>
</td>

<td align="center">
<img src="https://cdn.simpleicons.org/jinja/B41717" width="65"><br>
<b>Jinja2</b>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=git" width="65"><br>
<b>Git</b>
</td>

</tr>
</table>

</div>

---

<div align="center">

# Application Workflow

<img src="https://user-images.githubusercontent.com/74038190/212749726-d36b8253-74bb-450d-abbf-7d7cb8f4c8d5.gif" width="500">

</div>

```text
                Upload CSV
                     │
                     ▼
          Flask Receives File
                     │
                     ▼
        Load into Pandas DataFrame
                     │
                     ▼
      Dataset Profiling & Validation
                     │
     ┌───────────────┼────────────────┐
     ▼               ▼                ▼
 Summary Stats   Missing Values   Duplicates
     │               │                │
     └───────────────┼────────────────┘
                     ▼
       Correlation Analysis
                     │
                     ▼
      Distribution Visualization
                     │
                     ▼
        Outlier Detection (IQR)
                     │
                     ▼
       Rule-Based Smart Insights
                     │
                     ▼
       Interactive HTML Report
```

---

<div align="center">

# Project Architecture

</div>

```text
                    Browser
                       │
                       │
              Upload CSV Dataset
                       │
                       ▼
               Flask Application
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
     Pandas      Matplotlib      Seaborn
         │             │             │
         └─────────────┼─────────────┘
                       ▼
            Statistical Processing
                       │
          Summary • Charts • Insights
                       │
                       ▼
              Jinja2 HTML Templates
                       │
                       ▼
             Interactive Final Report
```

---

<div align="center">

# Project Structure

</div>

```text
csv-data-explorer/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── uploads/
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── templates/
│   ├── base.html
│   ├── upload.html
│   └── report.html
│
└── README.md
```

---

<div align="center">

# Installation

<img src="https://user-images.githubusercontent.com/74038190/212744286-4d65b0d0-3a70-4c3f-8f6b-0b2d7b8b6b64.gif" width="500">

</div>

### Clone Repository

```bash
git clone https://github.com/CodexxNinja/csv-data-explorer.git

cd csv-data-explorer
```

---

### Create Virtual Environment

**Windows**

```bash
python -m venv venv

venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_generated_secret_key
```

---

### Run Application

```bash
python app.py
```

---

### Open Browser

```
http://127.0.0.1:5000
```

Upload any CSV dataset and the application will immediately generate a complete analytical report with statistics, charts, outlier detection, and intelligent insights.

---

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212744289-38d25f79-2b2f-4a70-a2f5-c87dfc3e59d1.gif" width="100%">

</div>
<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212749695-042d7f9c-8c7d-4d17-9f45-f9dbb6f7a6f5.gif" width="70">

# How It Works

</div>

1. The user uploads a CSV file using the drag-and-drop interface or file picker.

2. Flask receives the uploaded file and securely loads it into a Pandas DataFrame.

3. The temporary uploaded file is immediately deleted after reading, ensuring no unnecessary data remains on the server.

4. The application profiles the dataset by calculating:

   * Number of rows and columns
   * Data types
   * Missing values
   * Duplicate rows
   * Descriptive statistics
   * Unique value counts

5. Numeric columns are analyzed to generate a correlation matrix and a Seaborn heatmap.

6. The visualization engine automatically ignores:

   * Constant columns
   * Identifier-like columns
   * Features that provide little analytical value

7. Distribution plots are generated for the most informative columns. Highly skewed features automatically use logarithmic scaling for better visualization.

8. Every numeric column is scanned for statistical outliers using the Interquartile Range (IQR) method.

9. A rule-based insight engine converts statistical findings into plain-English observations, highlighting:

   * Strongest correlations
   * Columns with the most missing values
   * Duplicate records
   * Skewed distributions
   * Potential data quality issues

10. Charts are rendered entirely in memory, encoded as Base64 images, and embedded directly into the report without creating image files.

11. The complete analytical report is displayed in a single interactive webpage.

---

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212744286-4d65b0d0-3a70-4c3f-8f6b-0b2d7b8b6b64.gif" width="70">

# Key Highlights

</div>

* Automatic dataset profiling
* Statistical summaries
* Missing value analysis
* Duplicate record detection
* Correlation heatmaps
* Intelligent distribution plots
* Rule-based analytical insights
* IQR-based outlier detection
* Interactive data preview
* Secure temporary file handling
* In-memory chart generation
* Responsive Flask interface

---

<div align="center">

# Contributing

Contributions, suggestions, and improvements are always welcome.

If you'd like to improve this project:

</div>

```bash
Fork the repository

Create a feature branch

Commit your changes

Push the branch

Open a Pull Request
```

---

<div align="center">

# License

This project is released under the **MIT License**.

You are welcome to use, modify, and learn from this project for educational and personal purposes.

</div>

---

<div align="center">

# Connect With Me

<a href="https://github.com/CodexxNinja">
<img src="https://img.shields.io/badge/GitHub-CodexxNinja-181717?style=for-the-badge&logo=github">
</a>

<a href="https://www.linkedin.com/">
<img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin">
</a>

<a href="mailto:paradkarvarad@gmail.com">
<img src="https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white">
</a>

</div>

---

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/216656965-39a36c9d-8db8-4a7e-9b8b-d59c79e5b8d3.gif" width="450">

### Thanks for visiting this repository.

If you found this project helpful, consider giving it a ⭐ on GitHub.

<img src="https://user-images.githubusercontent.com/74038190/216656977-ef584e23-480a-4d1f-8c3f-0f8d2b5b5f6b.gif" width="100%">

</div>
