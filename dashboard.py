# Memanggil semua library yang dibutuhkan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Title aplikasi
st.title("Dashboard Peminjaman Sepeda")

# Memuat dataset yang diunggah
hour_df = pd.read_csv('data_hour.csv')
day_df = pd.read_csv('data_day.csv')

# Tampilkan beberapa baris pertama dari dataset
st.subheader("Dataset Hour:")
st.dataframe(hour_df.head())  # Menampilkan dataset di Streamlit

st.subheader("Dataset Day:")
st.dataframe(day_df.head())  # Menampilkan dataset di Streamlit

# Informasi dataset
st.subheader("Informasi Dataset Hour:")
st.write(hour_df.info())  # Menampilkan info dataset di Streamlit

st.subheader("Informasi Dataset Day:")
st.write(day_df.info())  # Menampilkan info dataset di Streamlit

# Memeriksa missing values
st.subheader("Missing Values in Dataset Hour:")
st.write(hour_df.isna().sum())

st.subheader("Missing Values in Dataset Day:")
st.write(day_df.isna().sum())

# Parameter statistik dari dataset
st.subheader("Statistik Dataset Day:")
st.write(day_df.describe(include="all"))

st.subheader("Statistik Dataset Hour:")
st.write(hour_df.describe(include="all"))

# Mengubah kolom tanggal menjadi format datetime
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Mapping untuk kategorikal data
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
year_map = {0: 2011, 1: 2012}
holiday_map = {0: "Not Holiday", 1: "Holiday"}
workingday_map = {0: "Holiday", 1: "Working Day"}
weekday_map = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

day_df['season'] = day_df['season'].map(season_map)
day_df['yr'] = day_df['yr'].map(year_map)
day_df['holiday'] = day_df['holiday'].map(holiday_map)
day_df['workingday'] = day_df['workingday'].map(workingday_map)
day_df['weekday'] = day_df['weekday'].map(weekday_map)

# Menampilkan visualisasi distribusi data kategorikal
st.subheader("Distribusi Data Kategorikal Day Dataset:")
categorical_data = ["season", "yr", "holiday", "workingday", "weekday", "weathersit"]
for column in categorical_data:
    plt.figure(figsize=(8, 4))
    sns.histplot(day_df[column], kde=True)
    plt.title(f"Distribution of {column}")
    st.pyplot(plt)  # Menampilkan plot di Streamlit

# Pie chart untuk distribusi peminjaman sepeda
st.subheader("Distribusi Peminjaman Sepeda (Casual vs Registered):")
total_casual = day_df['casual'].sum()
total_registered = day_df['registered'].sum()

data = [total_casual, total_registered]
labels = ['Casual', 'Registered']

plt.figure(figsize=(6, 6))
plt.pie(data, labels=labels, autopct='%1.1f%%', colors=["#FF7F50", "#A52A2A"], startangle=90, explode=[0.05, 0], shadow=True)
plt.title('Distribusi Peminjaman Sepeda (Casual vs Registered)')
st.pyplot(plt)  # Menampilkan pie chart di Streamlit

# Bar plot untuk total penyewaan berdasarkan workingday dan tahun
st.subheader("Jumlah Total Sepeda yang Disewakan Berdasarkan Hari Kerja dan Tahun:")
working_counts = day_df.groupby(["workingday", "yr"])["cnt"].sum().reset_index()

plt.figure(figsize=(8, 4))
sns.barplot(data=working_counts, x="workingday", y="cnt", hue="yr", palette="viridis")
plt.title("Jumlah Total Sepeda yang Disewakan Berdasarkan Hari Kerja")
st.pyplot(plt)  # Menampilkan bar plot di Streamlit
