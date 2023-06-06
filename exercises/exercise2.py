import pandas as pd
import sqlite3

# Fetch the CSV data from the source URL
dtypes = {'EVA_NR': int, 'DS100': str, 'IFOPT': str, 'NAME': str, 'Verkehr': str, 'Laenge': float, 'Breite': float, 'Betreiber_Name': str, 'Betreiber_Nr': float}
csv_df = pd.read_csv('https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV', sep=';', decimal=',', dtype=dtypes)

# First, drop the "Status" column
csv_df = csv_df.drop('Status', axis=1)

#Drop all rows with invalid values:
#1. Valid "Verkehr" values are "FV", "RV", "nur DPN"
valid_verkehr_values = ["FV", "RV", "nur DPN"]

# Drop rows with invalid "Verkehr" values
csv_df = csv_df[csv_df["Verkehr"].isin(valid_verkehr_values)]

# 2. Valid "Laenge", "Breite" values are geographic coordinate system values between -90 and 90
# Remove columns with invalid values
csv_df = csv_df[(csv_df['Laenge'] >= -90) & (csv_df['Laenge'] <= 90)]
csv_df = csv_df[(csv_df['Breite'] >= -90) & (csv_df['Breite'] <= 90)]

#3. Valid "IFOPT" values follow this pattern:
#<exactly two characters>:<any amount of numbers>:<any amount of numbers><optionally another colon followed by any amount of numbers>

# Define the regex pattern for valid "IFOPT" values
pattern = r'^[A-Za-z]{2}:\d+:\d+(?::\d+)?$'

# Filter rows based on the specified "IFOPT" pattern
csv_df = csv_df[csv_df['IFOPT'].str.contains(pattern, na=False)]

#4. empty cells
csv_df = csv_df.dropna()

# Create a SQLite database and connect to it
conn = sqlite3.connect('trainstops.sqlite')

# Write the DataFrame to the SQLite database
csv_df.to_sql('trainstops', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()