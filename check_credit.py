'''
Gives the total of credits of a given period until the EOM from a starting date.
'''
from pandas import read_csv
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
#from parse_args import parse_args, dt


def first_day_of_the_month():
    return dt(dt.now().year, dt.now().month, 1)


def read_data_from_csv(csv_file):
    'Reads from the CSV file generated from the bank website'
    return read_csv(csv_file, parse_dates=['Date'], infer_datetime_format=True)


def next_month(date):
    "Returns the next month's date, from the first day"
    return date.replace(month=date.month + 1) if date.month < 12 else dt(date.year + 1, 1, 1)


def sum_from_the_date(data, date):
    'Sums up the total credit after a given date'
    return data.loc[(data['Date'] >= date) & (data['Date'] < next_month(date)), 'Credit'].sum()


def main(csv_file='Transactions.csv', date=first_day_of_the_month()):
    'Run the script to produce the total credit after the given date, inclusive'
    return f'${sum_from_the_date(read_data_from_csv(csv_file), date):,.2f}'


if __name__ == '__main__':
    print(main('Transactions.csv', dt.strptime('1/5/2018', '%d/%m/%Y')))
