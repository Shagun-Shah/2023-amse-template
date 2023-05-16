import pandas as pd
import csv
import sqlite3

# Fetch the data - Datasource1
excel_url = "https://opendata.stadt-muenster.de/sites/default/files/Fahrzeugbestand-Regierungsbezirk-Muenster-2018-2022.xlsx"

# Fetch the data - Datasource2
csv_url = "https://www.stadt-muenster.de/fileadmin/user_upload/stadt-muenster/61_stadtentwicklung/pdf/sms/05515000_csv_bevoelkerungsentwicklung_geschlecht.csv"

#Connect to the SQLite database
connection = sqlite3.connect('AMSE_database.db')

#Load into SQLite
excel_df = pd.read_excel(excel_url)
csv_df = pd.read_csv(csv_url, delimiter=';', encoding='latin-1')

excel_df.to_sql("Fahrzeugbestand Regierungsbezirk Münster 2018-2022", connection, if_exists='replace', index=False)
csv_df.to_sql("Opendata - Stadt Münster", connection, if_exists='replace', index=False)

connection.commit()

# Close the connection
connection.close()
