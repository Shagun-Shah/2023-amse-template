import os
import pytest
import pandas as pd
import pipeline


@pytest.fixture
def setup_data():
    """Fixture to set up data for testing"""
    pipeline.load_data()
    yield


def test_data_loading(setup_data: None):
    """Test if the data loading works and both datasets are instances of pandas.DataFrame"""
    assert isinstance(pipeline.csv_df_2020, pd.DataFrame)
    assert isinstance(pipeline.csv_df_2021, pd.DataFrame)


def test_dataframe_shapes(setup_data: None):
    """Test if the shapes of both dataframes are correct as expected"""
    expected_shapes = [(pipeline.csv_df_2020, (107907, 6)), (pipeline.csv_df_2021, (109880, 6))]

    for dataframe, expected_shape in expected_shapes:
        assert dataframe.shape == expected_shape


def test_dataframe_columns(setup_data: None):
    """Test if the columns of both dataframes are correct as expected"""
    expected_columns = [
        ['TATTAG', 'TATZEIT', 'TATORT', 'TATBESTANDBE_TBNR', 'GELDBUSSE', 'BEZEICHNUNG']
    ] * 2

    for dataframe, expected_column in zip((pipeline.csv_df_2020, pipeline.csv_df_2021), expected_columns):
        assert all(a == b for a, b in zip(dataframe.columns, expected_column))


def test_output_file_exists(setup_data: None):
    """Test if after the execution of the pipeline, both datasets are saved in an SQLite database file in the data directory"""
    directory_path = os.getcwd()
    assert os.path.exists(os.path.join(directory_path, "AMSE_database.sqlite"))


def run_tests():
    """Run all the tests and calculate the pass percentage"""
    tests = [
        test_data_loading,
        test_dataframe_shapes,
        test_dataframe_columns,
        test_output_file_exists
    ]

    total_tests = len(tests)
    passed_tests = 0

    for test in tests:
        try:
            test(setup_data)
            passed_tests += 1
            print(f"{test.__name__} passed.")
        except AssertionError:
            print(f"{test.__name__} failed.")

    pass_percentage = (passed_tests / total_tests) * 100
    print(f"Pass percentage: {pass_percentage}%")

    if pass_percentage == 100:
        print("All tests passed!")
    else:
        print("Some tests failed.")


if __name__ == "__main__":
    run_tests()