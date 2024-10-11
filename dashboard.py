# memanggil semua library yang dibutuhkan.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

import pandas as pd

# Memuat dataset day
path_dataset = "/content/data_day.csv"
day_df = pd.read_csv(path_dataset)
day_df.head()

import pandas as pd

# Memuat dataset hour
path_dataset = "/content/data_hour.csv"
hour_df = pd.read_csv(path_dataset)
hour_df.head()

# memeriksa tipe data dari kolom dalam day_df
day_df.info()

# memeriksa tipe data dari kolom dalam hour_df
hour_df.info()

# memeriksa missing value di dataset day_df dan hour_df
day_df.isna().sum()
hour_df.isna().sum()

# memeriksa duplikasi data
day_df.duplicated().sum()
hour_df.duplicated().sum()

# parameter statistik dari day_df
day_df.describe(include="all")

# parameter statistik dari hour_df
hour_df.describe(include="all")

day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

day_df.info()

hour_df.info()

day_df.describe(include="all")

# melakukan mapping pada day_df
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

# jenis data-data kategorikal dari day_df
categorical_data = ["season", "yr", "holiday", "workingday", "weekday", "weathersit"]

# subset untuk data kategorikal
daily_categorical_data = day_df[categorical_data]

for column in daily_categorical_data.columns:
    sns.histplot(daily_categorical_data[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.show()

hour_df.describe(include="all")

# melakukan mapping pada hour_df
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
year_map = {0: 2011, 1: 2012}
holiday_map = {0: "Not Holiday", 1: "Holiday"}
workingday_map = {0: "Holiday", 1: "Working Day"}
weekday_map = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

hour_df['season'] = hour_df['season'].map(season_map)
hour_df['yr'] = hour_df['yr'].map(year_map)
hour_df['holiday'] = hour_df['holiday'].map(holiday_map)
hour_df['workingday'] = hour_df['workingday'].map(workingday_map)
hour_df['weekday'] = hour_df['weekday'].map(weekday_map)

# jenis data-data kategorikal dari hour_df
categorical_data = ["season", "yr", "holiday", "workingday", "weekday", "weathersit"]

# subset untuk data kategorikal
daily_categorical_data = hour_df[categorical_data]

for column in daily_categorical_data.columns:
    sns.histplot(daily_categorical_data[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.show()

import matplotlib.pyplot as plt

# Menjumlahkan semua elemen dalam kolom casual
total_casual = day_df['casual'].sum()

# Menjumlahkan semua elemen dalam kolom registered
total_registered = day_df['registered'].sum()

# Membuat data untuk pie plot
data = [total_casual, total_registered]
labels = ['Casual', 'Registered']

# Membuat pie plot
plt.figure(figsize=(6, 6))  # Ukuran pie chart
plt.pie(data, labels=labels, autopct='%1.1f%%', colors=["#FF7F50", "#A52A2A"], startangle=90, explode=[0.05, 0], shadow=True)

# Menambahkan judul
plt.title('Distribusi Peminjaman Sepeda (Casual vs Registered)')

# Menampilkan pie plot
plt.show()

# Menghitung total penyewaan sepeda berdasarkan workingday dan tahun
working_counts = day_df.groupby(["workingday", "yr"])["cnt"].sum().reset_index()

# Membuat plot bar
sns.barplot(data=working_counts, x="workingday", y="cnt", hue="yr", palette="viridis")

# Mengatur judul dan label sumbu
plt.title("Jumlah total sepeda yang disewakan berdasarkan hari kerja")
plt.ylabel("Jumlah")

# Tampilkan plot
plt.show()

season_counts = day_df.groupby("season")["cnt"].sum().sort_values(ascending=False).reset_index()
season_counts.head()

temp_counts = hour_df.groupby("temp")["cnt"].sum().sort_values(ascending=False).reset_index()
temp_counts.head()
