import locale
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd


def find_mean(df):
    mean = round(df['Loan Amount(in USD)'].mean())
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    formatted_mean = locale.currency(mean, grouping=True)
    return formatted_mean

def find_median(df):
    median = round(df['Loan Amount(in USD)'].median())
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    formatted_median = locale.currency(median, grouping=True)
    return formatted_median

def find_std(df):
    std = round(df['Loan Amount(in USD)'].std())
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    formatted_std = locale.currency(std, grouping=True)
    return formatted_std

def currency_formatter(x,pos):
    if pos:
        return f"${int(x):,}"

def create_graph1(df):
    cost = df.groupby('School Country')['Loan Amount(in USD)'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.suptitle('Total Expenses by Country')
    plt.bar(
        cost['School Country'],
        cost['Loan Amount(in USD)'],
        color='orange'
    )
    plt.xlabel('School Country')
    plt.ylabel('Total Expenses')
    plt.xticks(rotation=90)  
    ax.yaxis.set_major_formatter(FuncFormatter(currency_formatter))
    plt.tight_layout()
    plt.savefig('total_expenses_by_country.png')

def create_graph2(df):
    df['Cost Per Year'] = df['Loan Amount(in USD)'] / df['Study Duration(in years)']
    cost_bins = [0, 20000, 40000, 60000, 80000]
    cost_labels = ['0-20,000(USD)', 
                   '20,000-40,000(USD)', 
                   '40,000-60,000(USD)', 
                   '60,000-$0,000(USD)'
                   ]
    df['Cost Range'] = pd.cut(df['Cost Per Year'], bins=cost_bins, labels=cost_labels)
    cost_range_counts = df['Cost Range'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(cost_range_counts, 
            labels=cost_labels, 
            autopct='%1.1f%%', 
            startangle=140
            )

    plt.title('Distribution of Students by Cost Range per Year. Total students: 422')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('by_year.png')
