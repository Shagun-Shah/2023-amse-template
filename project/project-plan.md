# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This project explores the Warnings and fines for stationary traffic (parking violations) for the years 2020 and 2021 for the city Bonn in the state North Rhine-Westphalia of Germany. We can obtain answers to the following questions by analysing the data:

* An increase in the overall amount of parking fines.
* Are there certain days or hours of the week when parking violations are more common? 
* Specific locations or areas where parking violations are more frequent in 2020 and 2021.


## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
a. We can gain a comprehensive understanding of parking behavior and its enforcement trends during this period.<br>

b. This analysis will enable authorities to make data-driven decisions, optimize enforcement efforts, and implement targeted interventions to improve parking compliance and ensure effective utilization of parking spaces in the future.


## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Verwarn- und Bußgelder ruhender Verkehr (Parkverstöße) 2020
* Metadata URL: https://mobilithek.info/offers/-6571901671376151135
* Data URL: https://opendata.bonn.de/sites/default/files/ParkverstoesseBonn2020_0.csv
* Data Type: CSV
* Columns: day, time, location, offense number, amount of the fine and vehicle type (car/truck)

 :arrow_right: The data set contains the warnings and fines (knolls/tickets) issued for parking violations in 2020 in the Bonn city area.

### Datasource2: Verwarn- und Bußgelder ruhender Verkehr (Parkverstöße) 2021
* Metadata URL: https://mobilithek.info/offers/-4923391267684416470
* Data URL: https://opendata.bonn.de/sites/default/files/Parkverst%C3%B6%C3%9Fe%202021.csv
* Data Type: CSV
* Columns: day, time, location, offense number, amount of the fine and vehicle type (car/truck)

:arrow_right: The data set contains the warnings and fines (knolls/tickets) issued for parking violations in 2021 in the Bonn city area.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Creation of Project Plan
2. Build an automated data pipeline
3. Work on exploratory data analysis
4. Update project plan and work packages
5. Automated tests for the project
6. CI for the project
7. Deployment of the project

[i1]: https://github.com/jvalue/2023-amse-template/issues/1
