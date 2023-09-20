import locale
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

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

def create_graph(df):
    country_expenses = df.groupby('School Country')['Loan Amount(in USD)'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.suptitle('Total Expenses by Country')
    plt.bar(country_expenses['School Country'], country_expenses['Loan Amount(in USD)'], color='blue')
    plt.xlabel('School Country')
    plt.ylabel('Total Expenses')
    plt.xticks(rotation=90)  
    ax.yaxis.set_major_formatter(FuncFormatter(currency_formatter))
    plt.tight_layout()
    plt.savefig('total_expenses_by_country.png')