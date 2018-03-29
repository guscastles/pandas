from functools import partial
import pandas as pd
from datetime import datetime as dt


def immutable(func):
    'Decorator that guarantees the immutability of the dataframe'

    def __wrapper__(*args):
        return func(args[0][:])

    return __wrapper__


@immutable
def change_date_column_to_datetime(data):
    'Changes all the values in the Date column from str to datetime'

    def __change__(index):
        data.loc[index, 'Date'] = dt.strptime(data.loc[index, 'Date'], '%d/%m/%Y')
    
    list(map(__change__, range(data.shape[0])))
    return data


def read_data_from_csv(csv_file):
    'Reads from the CSV file generated from the bank website'
    return pd.read_csv(csv_file)


def sum_from_the_date(data, date):
    'Sums up the total credit after a given date'
    return data.loc[data['Date'] >= date, 'Credit'].sum() 


def main(csv_file, date):
    'Run the script to produce the total credit after the given date, inclusive' 
    return sum_from_the_date(change_date_column_to_datetime(read_data_from_csv(csv_file)), date)


if __name__ == '__main__':
    CSV_FILE = '/home/gustavo/Downloads/Transactions.csv'
    print(main(CSV_FILE, dt(2018, 3, 1)))
