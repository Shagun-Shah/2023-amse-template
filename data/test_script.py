import os
import pandas as pd
import pipeline

def test_data_load():
    """ Test if the data loading works and both datasets are an object of class pandas.DataFrame """
    assert isinstance(pipeline.csv_df_2020, pd.DataFrame)
    assert isinstance(pipeline.csv_df_2021, pd.DataFrame)

def test_dataframe_shape():
    """ Test if the shapes of both dataframes are correct as expected """
    csv_df_2020_expected_shape = (107907, 6) # expected shape of the dataframe 1
    csv_df_2021_expected_shape = (109880, 6) # expected shape of the dataframe 2

    csv_df_2020_actual_shape = pipeline.csv_df_2020.shape # actual shape of the dataframe 1
    csv_df_2021_actual_shape = pipeline.csv_df_2021.shape # actual shape of the dataframe 2
    # check if the shape is correct
    assert len(csv_df_2020_actual_shape) == 2
    assert len(csv_df_2021_actual_shape) == 2 
    assert csv_df_2020_expected_shape[0] == csv_df_2020_actual_shape[0] 
    assert csv_df_2021_expected_shape[1] == csv_df_2021_actual_shape[1]
    assert csv_df_2020_expected_shape[0] == csv_df_2020_actual_shape[0]
    assert csv_df_2021_expected_shape[1] == csv_df_2021_actual_shape[1]
def test_dataframe_columns():
    """ Test if the columns of both dataframes are correct as expected """
    csv_df_2020_expected_columns = ['TATTAG', 'TATZEIT', 'TATORT', 'TATBESTANDBE_TBNR', 'GELDBUSSE', 'BEZEICHNUNG'] # expected columns of dataframe 1
    csv_df_2021_expected_columns = ['TATTAG', 'TATZEIT', 'TATORT', 'TATBESTANDBE_TBNR', 'GELDBUSSE', 'BEZEICHNUNG'] 
    csv_df_2020_actual_columns = pipeline.csv_df_2020.columns # actual columns of dataframe 1
    csv_df_2021_actual_columns = pipeline.csv_df_2021.columns # actual columns of dataframe 2
    # check if the columns are correct
    assert len(csv_df_2020_actual_columns) == len(csv_df_2020_expected_columns)
    assert all([a == b for a, b in zip(csv_df_2020_actual_columns, csv_df_2020_expected_columns)])
    assert len(csv_df_2021_actual_columns) == len(csv_df_2021_expected_columns)
    assert all([a == b for a, b in zip(csv_df_2021_actual_columns, csv_df_2021_expected_columns)])

def test_output_exists():
    """ Test if after the execution of the pipeline, both datasets are safed in an sqlite database file in the data directory """
    directory_path = os.getcwd() # get directory path
    assert os.path.exists(os.path.join(directory_path,"AMSE_database.sqlite"))
    #assert os.path.exists(os.path.join(directory_path,"e_ladesäulenregister.sqlite"))
def test_pipeline():
    """ Test if the pipeline script works as expected """
    test_output_exists()
    test_data_load()
    test_dataframe_shape()
    test_dataframe_columns()

if __name__ == "__main__":
    print("Start testing pipeline ...")
    test_pipeline()
    print("Test done!")