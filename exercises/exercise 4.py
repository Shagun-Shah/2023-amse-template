import urllib.request
import zipfile
import os
import pandas as pd
from sqlalchemy import create_engine

# Download and unzip data
url = 'https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip'
target_dir = 'data'

with urllib.request.urlopen(url) as response, open('temp.zip', 'wb') as f:
    f.write(response.read())

with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
    zip_ref.extractall(target_dir)

# Read and reshape data
csv_filename = os.path.join(target_dir, os.listdir(target_dir)[0])
columns_to_keep = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]
df = pd.read_csv(csv_filename, sep=';', decimal=',', usecols=columns_to_keep)
df.rename(columns={'Temperatur in °C (DWD)': 'Temperatur', 'Batterietemperatur in °C': 'Batterietemperatur'}, inplace=True)

# Transform data
df[['Temperatur', 'Batterietemperatur']] = df[['Temperatur', 'Batterietemperatur']].apply(lambda x: (x * 9/5) + 32)

# Validate data
df = df[(df['Monat'] >= 1) & (df['Monat'] <= 12)]
df = df[df['Geraet'] >= 0]

# Write data to SQLite database
engine = create_engine("sqlite:///temperatures.sqlite", echo=True)
df.to_sql('temperatures', engine, if_exists='replace', index=False)