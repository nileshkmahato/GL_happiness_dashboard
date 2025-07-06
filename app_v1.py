import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Global Happiness & Development Dashboard", layout="wide")

# --- DATA LOAD ---
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/canzafar/World-Happiness-Report/main/2023.csv"
    return pd.read_csv(url)

df = load_data()
df.rename(columns={
    "Country name": "Country",
    "Ladder score": "Happiness Score",
    "Logged GDP per capita": "GDP per Capita",
    "Social support": "Social Support",
    "Healthy life expectancy": "Life Expectancy",
    "Freedom to make life choices": "Freedom",
    "Perceptions of corruption": "Corruption",
    "Generosity": "Generosity"
}, inplace=True)

indicators = ["Happiness Score", "GDP per Capita", "Social Support", "Life Expectancy", "Freedom", "Corruption", "Generosity"]

# --- SIDEBAR ---
st.sidebar.header("🌐 Filters")
selected_country = st.sidebar.selectbox("Choose a Country", df["Country"].unique())
selected_indicators = st.sidebar.multiselect("Choose Indicators", indicators, default=["Happiness Score"])
st.sidebar.download_button("📥 Download CSV", df.to_csv(index=False), file_name="world_happiness_2023.csv")

# --- MAIN PANEL ---
st.title("🌍 Global Happiness & Development Dashboard")
st.markdown("Visualize and explore the **2023 World Happiness Report** and development indicators across countries.")

# Score for selected country
col1, col2 = st.columns([1, 3])
with col1:
    st.metric(label=f"Happiness Score in {selected_country}", value=round(df[df['Country'] == selected_country]['Happiness Score'].values[0], 2))

with col2:
    fig = px.choropleth(df, locations="Country", locationmode="country names",
                        color="Happiness Score", color_continuous_scale="Viridis",
                        title="World Happiness Scores (2023)")
    st.plotly_chart(fig, use_container_width=True)

# --- CORRELATION MATRIX ---
if len(selected_indicators) > 1:
    st.subheader("🔗 Correlation Matrix")
    corr = df[selected_indicators].corr()
    fig_corr, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig_corr)
else:
    st.info("Select at least two indicators to view correlation matrix.")

# --- TIME SERIES PLACEHOLDER ---
st.subheader("📈 Time Series (Coming Soon!)")
st.caption("We'll integrate time-based trends as soon as historical data is ingested.")

# --- FOOTER ---
st.markdown("---")
st.markdown("👥 Built by Group 7: Dheeraj, Nilesh, Neha, Pooja")
