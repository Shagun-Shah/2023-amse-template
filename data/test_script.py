import os
import pytest
import pandas as pd
import pipeline


@pytest.fixture
def setup_data():
    """Fixture to set up data for testing"""
    pipeline.load_data()
    yield


def test_data_load(setup_data):
    """Test if the data loading works and both datasets are instances of pandas.DataFrame"""
    assert isinstance(pipeline.csv_df_2020, pd.DataFrame)
    assert isinstance(pipeline.csv_df_2021, pd.DataFrame)


def test_dataframe_shape(setup_data):
    """Test if the shapes of both dataframes are correct as expected"""
    expected_shapes = [(pipeline.csv_df_2020, (107907, 6)), (pipeline.csv_df_2021, (109880, 6))]

    for dataframe, expected_shape in expected_shapes:
        assert dataframe.shape == expected_shape


def test_dataframe_columns(setup_data):
    """Test if the columns of both dataframes are correct as expected"""
    expected_columns = [
        ['TATTAG', 'TATZEIT', 'TATORT', 'TATBESTANDBE_TBNR', 'GELDBUSSE', 'BEZEICHNUNG']
    ] * 2

    for dataframe, expected_column in zip((pipeline.csv_df_2020, pipeline.csv_df_2021), expected_columns):
        assert all(a == b for a, b in zip(dataframe.columns, expected_column))


def test_output_exists(setup_data):
    """Test if after the execution of the pipeline, both datasets are saved in an SQLite database file in the data directory"""
    directory_path = os.getcwd()
    assert os.path.exists(os.path.join(directory_path, "AMSE_database.sqlite"))


def test_pipeline():
    """Test if the pipeline script works as expected"""
    test_data_load()
    test_dataframe_shape()
    test_dataframe_columns()
    test_output_exists()
