import streamlit as st
import pandas as pd
import plotly.express as px

# Load data directly from GitHub (2023 World Happiness Report)
url = "https://raw.githubusercontent.com/canzafar/World-Happiness-Report/main/2023.csv"
df = pd.read_csv(url)

# Show a simple dashboard
st.title("🌍 World Happiness Dashboard")

# Select country and show happiness score
country = st.selectbox('Select Country', df['Country name'].unique())
score = df[df['Country name'] == country]['Ladder score'].values[0]
st.write(f"Happiness Score for {country} in 2023: **{score:.2f}**")

# Show world map
fig = px.choropleth(
    df,
    locations="Country name",
    locationmode="country names",
    color="Ladder score",
    color_continuous_scale="Viridis",
    title="World Happiness Scores 2023"
)
st.plotly_chart(fig)