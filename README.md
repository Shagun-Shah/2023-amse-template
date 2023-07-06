# AMSE/SAKI 2023 Template Project
I am presenting my AMSE/SAKI module 2023 submission through this repository. It is a clone of the [template project](https://github.com/jvalue/2023-amse-template)

Within this repository, you can find two components: 

- A data science project that was developed throughout the semester, and 
- The exercises that were submitted during the semester.

## Project Setup
The following files are part of the final project:

- `AMSE_database.sqlite`:  This file contains the processed dataset. Initially, an automated data pipeline is created that will further create this SQLite database to retrieve data from multiple open data sources. This repository includes data about Warnings and fines for stationary traffic (parking violations) for the years 2020 and 2021 for the city Bonn in the state North Rhine-Westphalia of Germany.

- `exploration.ipynb`: A Jupyter notebook is used to explore the data and show in detail what it looks like. It contains detailed information about the datasets with some visualizations.

- `report.ipynb`: The Jupyter notebook serves as the final report, presenting the project's question along with its conclusive answer. To convey the answer effectively, bar graphs is employed as visualizations to represent the results, based on the data in `AMSE_database.sqlite`.


## Exercises

Within the repository's `exercises` folder, it contains the completed exercises that were assigned throughout the semester. By the end of the semester, the repository consists of the following files:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.py`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.py`
5. `./exercises/exercise5.jv`

### Exercise Feedback
Automated exercise feedback was provided through out the semester for each exercise using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). To view exercise feedback, navigate to Actions -> Exercise Feedback in the repository.

The exercise feedback is executed whenever any changes are made in files in the `exercise` folder and in case of pushing the local changes to the repository on GitHub. 

The automated exercise feedback is:

```sh
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13

Grading Exercise 2
	Overall points 24 of 24
	---
	By category:
		Shape: 5 of 5
		Types: 17 of 17
		Quality: 2 of 2

Grading Exercise 3
	Overall points 22 of 22
	---
	By category:
		Shape: 4 of 4
		Types: 14 of 14
		Quality: 4 of 4

Grading Exercise 4
	Overall points 15 of 15
	---
	By category:
		Shape: 4 of 4
		Types: 9 of 9
		Quality: 2 of 2

Grading Exercise 5
	Overall points 14 of 14
	---
	By category:
		Shape: 4 of 4
		Types: 5 of 5
		Quality: 5 of 5
```
