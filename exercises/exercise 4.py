import zipfile
import urllib.request
import pandas as pd
import sqlite3

# 1: Download and unzip data
zip = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
zip_path = "mowesta-dataset.zip"
csv_file = "data.csv"

urllib.request.urlretrieve(zip, zip_path)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extract(csv_file)

# 2: Reshape data
columns = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]
new_column_names = {"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"}

df = pd.read_csv(csv_file, delimiter=';', index_col=False, usecols=columns)
df.rename(columns=new_column_names, inplace=True)

# 3: Transform data
# Celsius to Fahrenheit
df["Temperatur"] = df["Temperatur"].astype(str).apply(lambda x: float(x.replace(',', '.')))
df["Batterietemperatur"] = df["Batterietemperatur"].astype(str).apply(lambda x: float(x.replace(',', '.')))

# Celsius to Fahrenheit
df["Temperatur"] = (df["Temperatur"] * 9/5) + 32
df["Batterietemperatur"] = (df["Batterietemperatur"] * 9/5) + 32

# 4: Validate data
# Data Type Validation
df = df.astype({
    "Geraet": int,
    "Monat": int,
    "Geraet aktiv": str })

# Fahrenheit Temperature Validation
valid_temp_range = (-459.67, 212)
temp_valid = df["Temperatur"].between(*valid_temp_range)
df = df[temp_valid]

# Batterietemperatur Validation
valid_battery_range = df["Batterietemperatur"].between(*valid_temp_range)
df = df[valid_battery_range]

# 5: Write data to SQLite database
db_name = "temperatures.sqlite"
table_name = "temperatures"
connection = sqlite3.connect(db_name)
df.to_sql(table_name, connection, if_exists='replace', index=False)
connection.close()