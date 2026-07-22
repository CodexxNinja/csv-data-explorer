# <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Magnifying%20Glass%20Tilted%20Left.png" alt="Magnifying Glass" width="40" height="40" /> CSV Data Explorer

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212750342-3d7c7b2d-f0a8-43b7-b2c9-6d3b0b6d4d63.gif" width="700" alt="CSV Data Explorer Demo"/>
</p>

<p align="center">
  <strong>Intelligent CSV Analysis using Flask, Pandas & Data Visualization</strong>
</p>

<p align="center">
  Automatically transform any uploaded CSV file into a comprehensive analytical report featuring descriptive statistics, automated distribution charts, correlation heatmaps, rule-based insights, and IQR outlier detection.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask" alt="Flask"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas" alt="Pandas"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge" alt="Matplotlib"/>
  <img src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge" alt="Seaborn"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
</p>

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmarks.png" alt="Overview" width="28" height="28" /> Overview

**CSV Data Explorer** is an automated web-based analytical tool designed to bridge the gap between raw data collection and preliminary analysis. By uploading a standard CSV dataset, users receive a fully formatted, interactive HTML dashboard detailing distribution trends, data cleanliness, variable relationships, and anomaly occurrences—all without writing code.

> Developed during **Week 3** of the **Python → Flask → AI/ML Engineering Roadmap**.

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Laptop.png" alt="Demo" width="28" height="28" /> Live Demo

> **Hosted Application:** *Link to be added post-deployment.*

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Sparkles.png" alt="Key Features" width="28" height="28" /> Key Features

| Feature | Description |
| :--- | :--- |
| **Drag & Drop Upload** | Modern client-side UI with real-time file validation and drop-zone visual feedback. |
| **Dataset Profiling** | Instant summaries covering total rows, dimensions, inferenced data types, and unique counts. |
| **Missing Data Audit** | Column-level integrity reporting to identify incomplete records and missingness ratios. |
| **Correlation Analysis** | Automatic generation of interactive/static Pearson correlation heatmaps for numeric features. |
| **Visual Distributions** | Tailored chart rendering (histograms, kernel density estimates, box plots) per column type. |
| **Outlier Detection** | Interquartile Range (IQR) implementation to flag extreme values across dataset variables. |
| **Automated Insights** | Rule-based engine rendering clear textual observations regarding data distribution and quality. |
| **Interactive Preview** | Paginated table display presenting the initial records of the uploaded file. |
| **Privacy & Cleanup** | Automatic server-side file purge upon report generation for secure processing. |

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Tech/Gear.png" alt="Tech Stack" width="28" height="28" /> Tech Stack Architecture

* **Backend Engine:** Python 3.10+, Flask
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Frontend Design:** HTML5, CSS3, JavaScript (ES6)
* **Templating:** Jinja2

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Diagrams/Flowchart.png" alt="Workflow" width="28" height="28" /> Application Workflow

```text
               +-----------------------+
               |   CSV File Uploaded   |
               +-----------+-----------+
                           |
                           v
               +-----------------------+
               |   Flask Route Engine  |
               +-----------+-----------+
                           |
                           v
         +-----------------------------------+
         |     Pandas Processing Engine      |
         +-----------------+-----------------+
                           |
   +-----------------------+-----------------------+
   |                       |                       |
   v                       v                       v
[ Profiling ]       [ Visualizations ]      [ IQR Outliers ]
* Shape & Dtypes    * Histograms            * Bounds Calculation
* Null Auditing     * Heatmaps              * Anomaly Flagging
* Unique Values     * Box Plots             * Rule-Based Insights
   |                       |                       |
   +-----------------------+-----------------------+
                           |
                           v
               +-----------------------+
               |   Jinja2 Rendering    |
               +-----------+-----------+
                           |
                           v
               +-----------------------+
               | HTML Interactive Dashboard |
               +-----------------------+
