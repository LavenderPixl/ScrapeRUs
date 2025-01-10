import csv
import pandas as pd
import os.path

file_name = "VisitedSites.csv"

fields = ['Url', 'Domain', 'Allowed', 'Disallowed']
rows = []


def csv_start_up():
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as csv_file:
            writer = csv.writer(csv_file)
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
            writer = csv.writer(csv_file)
            writer.writerow(i)
        rows_added += 1

    print(f"Rows added: {rows_added}")

def check_if_exists(file, domain):
    data_frame = pd.read_csv(file)
    if domain.url in data_frame['Url'].unique():
        return True
    return False

def print_csv_data():
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)
