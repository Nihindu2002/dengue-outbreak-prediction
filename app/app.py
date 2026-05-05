import streamlit as st
import pandas as pd
import joblib
import folium
from streamlit_folium import st_folium
import json, numpy as np

st.set_page_config(page_title="Dengue Early Warning", layout="wide")
st.title("🦟 Dengue Outbreak Early Warning System — Sri Lanka")

df = pd.read_csv('data/dengue_features.csv')
model = joblib.load('models/rf_model.pkl')
geo = json.load(open('data/lka_districts.geojson', 'r'))

# Prepare features with one-hot encoding for City
df_processed = df.copy()
df_processed = pd.get_dummies(df_processed, columns=['City'], drop_first=False)

district = st.sidebar.selectbox("Select District", sorted(df['District'].unique()))
df_d = df_processed[df['District'] == district]

st.subheader(f"Cases Over Time — {district}")
st.line_chart(df[df['District'] == district].set_index('Date')['Dengue_Cases'])

# Alert
latest = df_d.sort_values('Date').iloc[-1]
# Use only the features the model expects
feature_cols = model.feature_names_in_
X_pred = latest[feature_cols].to_frame().T
prob = model.predict_proba(X_pred)[0][1]

if prob > 0.7:
    st.error(f"🔴 HIGH RISK — Outbreak probability: {prob:.0%}")
elif prob > 0.4:
    st.warning(f"🟡 MEDIUM RISK — Outbreak probability: {prob:.0%}")
else:
    st.success(f"🟢 LOW RISK — Outbreak probability: {prob:.0%}")

st.subheader("District Risk Map")
m = folium.Map(location=[7.8731, 80.7718], zoom_start=7)
district_totals = df.groupby('District')['Dengue_Cases'].sum().reset_index()
# Add " District" suffix to match GeoJSON naming
district_totals['GeoName'] = district_totals['District'] + ' District'
folium.Choropleth(geo_data=geo, data=district_totals,
    columns=['GeoName','Dengue_Cases'], key_on='feature.properties.shapeName',
    fill_color='YlOrRd', legend_name='Total Cases').add_to(m)
st_folium(m, width=700, height=450)