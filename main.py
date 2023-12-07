# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import argparse
import datetime

import pandas as pd

base_url = "http://www.adventskalender-eichstaett.eu/"


def get_subsite_win(day, number):
    print(f"Tag {day}")
    prefix = "12"
    if day < 10:
        prefix = "120"
    converted_day = prefix + str(day)
    tables = pd.read_html(f'{base_url}{converted_day}')  # Returns list of all tables on page
    for table in tables:
        row = table.loc[:, table.columns.isin(["LOS"])]
        if len(row) > 1:
            winning_row = table[table[1].str.contains(number)]
            return winning_row


# Press the green button in the gutter to run the script.
def check_winners(number):
    today = datetime.datetime.today().day
    for x in range(1, today + 1):
        winning_row = get_subsite_win(x, number)
        if winning_row is not None and len(winning_row.values) > 0:
            print(f"--> Yay, du hast gewonnen: {winning_row.iloc[0, 0]} - {winning_row.iloc[0, 1]} - {winning_row.iloc[0, 2]}"
                  f" - {winning_row.iloc[0, 3]}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', help='Deine Adventskalender ID')
    args = parser.parse_args()

    if ',' in args.number:
        my_ids = args.number.split(",")
        for id in my_ids:
            print(f'Deine Id: {id}')
            check_winners(id)
    else:
        print(f'Deine Id: {args.number}')
        check_winners(args.number)
