# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This project analyses the connection between Münster's population and demographic composition, vehicle type, and vehicle quantity.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
We can better comprehend the relationship between population growth and the number of automobiles on city roads over time by analysing these two variables. 
To find correlations and patterns, this analysis may involve examining population growth trends and statistics on car stock over a number of years, preferred vehicle type amongst the age group.


## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Fahrzeugbestand Regierungsbezirk Münster 2018-2022
* Metadata URL: https://mobilithek.info/offers/-1738218276875079533
* Data URL: https://opendata.stadt-muenster.de/sites/default/files/Fahrzeugbestand-Regierungsbezirk-Muenster-2018-2022.xlsx
* Data Type: XLSX

 Information on the vehicle stock in the administrative district of Münster in the years 2018-2022.

### Datasource2: Opendata - Stadt Münster
* Metadata URL: https://opendata.stadt-muenster.de/dataset/statistik-bev%C3%B6lkerungsentwicklung
* Data URL: https://www.stadt-muenster.de/fileadmin/user_upload/stadt-muenster/61_stadtentwicklung/pdf/sms/05515000_csv_bevoelkerungsentwicklung_geschlecht.csv
* Data Type: CSV

The CSV file "Statistics - Population Development by Gender" contains attributes Time, Area, Characteristic (Male, Female), Value.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Explore more datasets for this project --> Data Collection
2. Data Cleaning & Data Integration
3. Data Transformation
4. Build an automated data pipeline
5. Automated tests for the project
6. CI for the project
7. Deployment
8. Data Visualization

[i1]: https://github.com/jvalue/2023-amse-template/issues/1
