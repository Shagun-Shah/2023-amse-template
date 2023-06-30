import os
import zipfile
import urllib.request
import pandas as pd
from sqlalchemy import BIGINT, TEXT, FLOAT

# 1: Download and unzip data
zip_file, headers = urllib.request.urlretrieve('https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip')

with zipfile.ZipFile(zip_file, "r") as zip_ref:
    target_dir = "data"
    zip_ref.extractall(target_dir)
csv_file = os.path.join(target_dir, os.listdir(target_dir)[0])

# 2: Reshape data
df = pd.read_csv(csv_file, sep=';', decimal=',', index_col=False, usecols=["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"])

df = df.rename(columns={'Temperatur in °C (DWD)': 'Temperatur','Batterietemperatur in °C': 'Batterietemperatur'})

# 3: Transform data
# Celsius to Fahrenheit
df["Temperatur"] = df["Temperatur"].astype(str).apply(lambda x: float(x.replace(',', '.')))
df["Batterietemperatur"] = df["Batterietemperatur"].astype(str).apply(lambda x: float(x.replace(',', '.')))

# Celsius to Fahrenheit
df["Temperatur"] = (df["Temperatur"] * 9/5) + 32
df["Batterietemperatur"] = (df["Batterietemperatur"] * 9/5) + 32

# 4: Validate 
df = df[ (df['Monat'] >= 1) & (df['Monat'] <= 12)]
df = df[ (df['Geraet'] >= 0)]


# 5: Use fitting SQLite types
df.to_sql('temperatures', 'sqlite:///temperatures.sqlite', if_exists='replace', index=False, dtype={
        'Geraet': BIGINT,
        'Hersteller': TEXT,
        'Model': TEXT,
        'Monat': BIGINT,
        'Temperatur': FLOAT,
        'Batterietemperatur': FLOAT,
        'Geraet aktiv': TEXT
    })