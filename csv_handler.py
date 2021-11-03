import csv


def append_row(csvfile_path, fieldnames, row):
    with open(csvfile_path, 'a', newline='') as csvfile:
        writer = create_writer(csvfile, fieldnames)
        writer.writerow(row)


def read_all_rows(csvfile_path, fieldnames):
    rows = []
    with open(csvfile_path, newline='') as csvfile:
        reader = create_reader(csvfile, fieldnames)
        for row in reader:
            rows.append(row)
    return rows

def create_reader(csvfile, fieldnames):
    return csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)


def create_writer(csvfile, fieldnames):
    return csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
