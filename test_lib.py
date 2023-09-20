from lib import find_mean, find_median, find_std
import pandas as pd

def test_stats():
    data = {'Loan Amount(in USD)': [1000, 2000, 3000, 4000, 5000]}
    df = pd.DataFrame(data)
    expected_mean = '$3,000.00'
    expected_median = '$3,000.00'
    expected_std =  '$1,581.00'
    
    mean_result = find_mean(df)
    median_result = find_median(df)
    std_result = find_std(df)
    
    assert mean_result == expected_mean
    assert median_result == expected_median
    assert std_result == expected_std

if __name__ == "__main__":
    test_stats()