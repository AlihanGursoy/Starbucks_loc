import streamlit as st
import pandas as pd

df=pd.read_json("https://raw.githubusercontent.com/mmcloughlin/starbucks/master/locations.json")

ulkeler=df['country'].unique()
ulkeler = sorted(ulkeler)
ulke=st.sidebar.selectbox("Ülke Seç",ulkeler)

df=df[df['country']==ulke]
sehirler=df['city'].unique()
sehirler = sorted(sehirler)

sehir=st.sidebar.selectbox("Şehir Seç", sehirler)
df=df[df['city']==sehir]

st.map(df[['latitude', 'longitude']])