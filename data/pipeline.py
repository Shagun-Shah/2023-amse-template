import pandas as pd
import sqlite3

# Fetch the data - Datasource1
csv_url_2020 = "https://opendata.bonn.de/sites/default/files/ParkverstoesseBonn2020_0.csv"

# Fetch the data - Datasource2
csv_url_2021 = "https://opendata.bonn.de/sites/default/files/Parkverst%C3%B6%C3%9Fe%202021.csv"

#Load into SQLite
csv_df_2020 = pd.read_csv(csv_url_2020, delimiter=';', encoding='utf-8')
csv_df_2021 = pd.read_csv(csv_url_2021, delimiter=';', encoding='latin-1')

#Data Transformation

#Renaming erroneous column name
csv_df_2020.rename(columns= {'ï»¿TATTAG':'TATTAG'}, inplace=True)

#Replacing column & row data errors
csv_df_2020.columns = csv_df_2020.columns.str.replace('Ã¼', 'ü')
csv_df_2020.columns = csv_df_2020.columns.str.replace('Ã', 'ß')
csv_df_2020.columns = csv_df_2020.columns.str.replace('Ã¤', 'ä')
column_name = 'TATORT'
csv_df_2020[column_name] = csv_df_2020[column_name].str.replace('ß¶', 'ö')
csv_df_2020.replace({'Ã¼': 'ü', 'Ã': 'ß', 'Ã¤': 'ä', 'ß¶': 'ö'}, regex=True, inplace=True)

#Connect to the SQLite database
connection = sqlite3.connect('AMSE_database.sqlite')

# Write DataFrame to SQLite tables
csv_df_2020.to_sql("Verwarn- und Bußgelder ruhender Verkehr (Parkverstöße) 2020", connection, if_exists='replace', index=False)
csv_df_2021.to_sql("Verwarn- und Bußgelder ruhender Verkehr (Parkverstöße) 2021", connection, if_exists='replace', index=False)

# Commit changes to the database
connection.commit()

# Close the connection
connection.close()