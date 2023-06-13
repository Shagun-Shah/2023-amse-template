import os
import pandas as pd
import pipeline


def test_data_load():
    """Test if the data loading works and both datasets are instances of pandas.DataFrame"""
    print("Testing data loading...")
    assert isinstance(pipeline.csv_df_2020, pd.DataFrame)
    assert isinstance(pipeline.csv_df_2021, pd.DataFrame)
    print("Data loading test passed!")


def test_dataframe_shape():
    """Test if the shapes of both dataframes are correct as expected"""
    print("Testing dataframe shapes...")
    csv_df_2020_expected_shape = (107907, 6)  # expected shape of the dataframe 1
    csv_df_2021_expected_shape = (109880, 6)  # expected shape of the dataframe 2

    csv_df_2020_actual_shape = pipeline.csv_df_2020.shape  # actual shape of the dataframe 1
    csv_df_2021_actual_shape = pipeline.csv_df_2021.shape  # actual shape of the dataframe 2

    # check if the shape is correct
    assert csv_df_2020_actual_shape == csv_df_2020_expected_shape
    assert csv_df_2021_actual_shape == csv_df_2021_expected_shape
    print("Dataframe shapes test passed!")


def test_dataframe_columns():
    """Test if the columns of both dataframes are correct as expected"""
    print("Testing dataframe columns...")
    csv_df_2020_expected_columns = [
        'TATTAG', 'TATZEIT', 'TATORT', 'TATBESTANDBE_TBNR', 'GELDBUSSE', 'BEZEICHNUNG'
    ]
    csv_df_2021_expected_columns = [
        'TATTAG', 'TATZEIT', 'TATORT', 'TATBESTANDBE_TBNR', 'GELDBUSSE', 'BEZEICHNUNG'
    ]
    csv_df_2020_actual_columns = pipeline.csv_df_2020.columns
    csv_df_2021_actual_columns = pipeline.csv_df_2021.columns

    # check if the columns are correct
    assert all(a == b for a, b in zip(csv_df_2020_actual_columns, csv_df_2020_expected_columns))
    assert all(a == b for a, b in zip(csv_df_2021_actual_columns, csv_df_2021_expected_columns))
    print("Dataframe columns test passed!")


def test_output_exists():
    """Test if after the execution of the pipeline, both datasets are saved in an SQLite database file in the data directory"""
    print("Testing pipeline output...")
    directory_path = os.getcwd()  # get directory path
    assert os.path.exists(os.path.join(directory_path, "AMSE_database.sqlite"))
    print("Pipeline output test passed!")


def test_pipeline():
    """Test if the pipeline script works as expected"""
    print("Start testing pipeline...")
    test_data_load()
    test_dataframe_shape()
    test_dataframe_columns()
    test_output_exists()
    print("Pipeline test done!")


if __name__ == "__main__":
    test_pipeline()
