import csv
import pandas as pd
import os.path

from pandas.errors import EmptyDataError

file_name = "VisitedSites.csv"

fields = ['Url', 'Domain', 'Allowed', 'Disallowed']
rows = []


def csv_start_up():
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=' ')
            writer.writerow(fields)
    return file_name


def add_to_csv(file, domains):
    rows_added = 0
    for domain in domains:
        exists = check_if_exists(file, domain)
        if exists:
            continue

        if domain.disallowed is None and domain.allowed is None:
            domain.disallowed = "Null"
            domain.allowed = "Null"

        i = [domain.url, domain.domain, domain.allowed, domain.disallowed]
        with open(file, 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=' ')
            writer.writerow(i)
        rows_added += 1

    print(f"Rows added: {rows_added}")


# def edit_row():


def check_if_exists(file, domain):
    try:
        data_frame = pd.read_csv(file)
        if data_frame is None or data_frame.empty:
            return False

        if domain.url in data_frame['Url'].unique():
            return True
        return False
    # If file is Empty
    except EmptyDataError:
        csv_start_up()
    # If Field does not exist (File incorrectly created.)
    except KeyError:
        os.remove(file)
        csv_start_up()


def print_csv_data():
    data_frame = pd.read_csv(file_name)
    print(data_frame)
