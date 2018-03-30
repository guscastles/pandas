'''
Gives the total of credits of a given period until the EOM from a starting date.
'''
import argparse
from datetime import datetime as dt
from pandas import read_csv


ARGS_LIST = [('file', 'The name of the CSV file from the bank website'),
             ('date', 'The start date. The period will be to the EOM (dd/mm/yyyy)')]
DESCRIPTION = 'We need a file and a date'


def read_data_from_csv(csv_file):
    'Reads from the CSV file generated from the bank website'
    return read_csv(csv_file, parse_dates=['Date'], infer_datetime_format=True)


def sum_from_the_date(data, date):
    'Sums up the total credit after a given date'
    next_month = date.replace(month=date.month + 1) if date.month < 12 else dt(date.year + 1, 1, 1)
    return data.loc[(data['Date'] >= date) & (data['Date'] < next_month), 'Credit'].sum()


def main(csv_file, date):
    'Run the script to produce the total credit after the given date, inclusive'
    return sum_from_the_date(read_data_from_csv(csv_file), date)


def parse_args():
    'Parses the command-line arguments, file and date'

    def __add_args__(parser, args):
        if args:
            parser.add_argument(args[0][0], help=args[0][1])
            __add_args__(parser, args[1:])
        return parser

    parser = __add_args__(argparse.ArgumentParser(description=DESCRIPTION), ARGS_LIST)
    args = parser.parse_args()
    return args.file, dt.strptime(args.date, '%d/%m/%Y')


if __name__ == '__main__':
    print(main(*parse_args()))
