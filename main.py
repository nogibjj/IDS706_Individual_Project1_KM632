import pandas as pd
from lib import find_mean, find_median, find_std, create_graph1,create_graph2

def prepare_dataset(file_path):
    df = pd.read_excel(file_path)
    new_column_names = {'Эцэг /эх/-ийн нэр / Өөрийн нэр': 'First and Last Name', 
                        'Суралцаж байгаа улс': 'School Country', 
                        'Сургуулийн нэр': 'School Name', 
                        'Мэргэжил':'Intended Major', 
                        'Суралцах хугацаа': 'Study Duration(in years)', 
                        'Олгосон санхүүжил':'Loan Amount(in USD)'
                        }
    df.rename(columns=new_column_names, inplace=True)
    
    mean = find_mean(df)
    median = find_median(df)
    std = find_std(df)
    create_graph1(df)
    create_graph2(df)
    
    print("Mean:", mean)
    print("Median:", median)
    print("Standard deviation:", std)
    return df

if __name__ == "__main__":
    df = prepare_dataset('raw.xlsx')