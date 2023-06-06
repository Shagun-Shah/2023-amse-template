import pandas as pd
from sqlalchemy import types, create_engine

# Fetch the CSV data from the source URL
d_types = {
    'EVA_NR': types.BIGINT,
    'DS100': types.TEXT,
    'IFOPT': types.TEXT,
    'NAME': types.TEXT,
    'Verkehr': types.TEXT,
    'Laenge': types.FLOAT,
    'Breite': types.FLOAT,
    'Betreiber_Name': types.TEXT,
    'Betreiber_Nr': types.BIGINT}

csv_df = pd.read_csv('https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV', sep=';', decimal=',')

# First, drop the "Status" column
csv_df = csv_df.drop('Status', axis=1)

#Drop all rows with invalid values:
# Valid "Verkehr" values are "FV", "RV", "nur DPN"
valid_verkehr_values = ["FV", "RV", "nur DPN"]

# Drop rows with invalid "Verkehr" values
csv_df = csv_df[csv_df["Verkehr"].isin(valid_verkehr_values)]

# Valid "Laenge", "Breite" values are geographic coordinate system values between -90 and 90
csv_df = csv_df[(csv_df['Laenge'] >= -90) & (csv_df['Laenge'] <= 90)]
csv_df = csv_df[(csv_df['Breite'] >= -90) & (csv_df['Breite'] <= 90)]

# Valid "IFOPT" values follow this pattern:
# <exactly two characters>:<any amount of numbers>:<any amount of numbers><optionally another colon followed by any amount of numbers>

# Define the regex pattern for valid "IFOPT" values
pattern = r'^[A-Za-z]{2}:\d+:\d+(?::\d+)?$'

# Filter rows based on the specified "IFOPT" pattern
csv_df = csv_df[csv_df['IFOPT'].str.contains(pattern, na=False)]

# Empty cells
csv_df = csv_df.dropna()

# Write the DataFrame to the SQLite database
engine = create_engine("sqlite:///trainstops.sqlite")
csv_df.to_sql('trainstops',engine ,  if_exists='replace',index= False, dtype= d_types)