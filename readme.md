# 🌍 Global Happiness & Development Dashboard

An interactive Streamlit-powered data visualization platform that helps users explore and understand the intricate relationships between global happiness levels and various development indicators like GDP, social support, life expectancy, and more.

Built by **Group 7**  
👤 Dheeraj Parui – 2021TM70858  
👤 Nilesh Mahato – 2021TM70864  
👤 Neha Godage – 2021TM70833  
👤 Pooja Balamkar – 2021TM70875  

## 🎯 Project Vision

To empower researchers, policymakers, educators, and the general public with an intuitive and interactive tool to visualize and analyze global happiness trends and development metrics — fostering data-driven insights and informed decisions.

---

## 📦 Features

- 🌐 **Interactive Choropleth Map** — Compare happiness scores globally
- 📊 **Multi-indicator Selection** — Analyze development indicators (GDP, Life Expectancy, etc.)
- 🔗 **Correlation Matrix** — Discover patterns between chosen indicators
- 🧮 **Country Filtering** — View scores and metrics for a selected country
- 💾 **CSV Export** — Download raw data with one click
- 🚧 **Future-Ready** — Time series support, user logins, and region filters planned

---

## 🚀 How to Use

### 1. ⚙️ Prerequisites

- Python 3.8+
- Virtual environment recommended

### 2. 💾 Installation

```bash
# Create and activate a virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# If requirements.txt isn't included, install manually:

pip install streamlit pandas plotly seaborn matplotlib


# ▶️ Run the App
streamlit run app.py


## This will launch the app locally
