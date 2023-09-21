import pytest
import pandas as pd
from main import prepare_dataset


TEST_FILE = "test_data.xlsx"

sample_data = {
    "Эцэг /эх/-ийн нэр / Өөрийн нэр": ["John Doe", "Jane Smith"],
    "Суралцаж байгаа улс": ["USA", "Canada"],
    "Сургуулийн нэр": ["School A", "School B"],
    "Мэргэжил": ["Computer Science", "Mathematics"],
    "Суралцах хугацаа": [4, 5],
    "Олгосон санхүүжил": [25000, 30000],
}


@pytest.fixture
def test_data(tmp_path):
    test_file_path = TEST_FILE
    df = pd.DataFrame(sample_data)
    df.to_excel(test_file_path, index=False)
    return test_file_path


def test_prepare_dataset(test_data):
    df = prepare_dataset(test_data)

    assert isinstance(df, pd.DataFrame), "Expected a DataFrame"

    expected_columns = [
        "First and Last Name",
        "School Country",
        "School Name",
        "Intended Major",
        "Study Duration(in years)",
        "Loan Amount(in USD)",
    ]
    assert all(col in df.columns for col in expected_columns), "Missing columns"
