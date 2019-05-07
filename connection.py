import csv

def read_data(filename):
    with open(filename, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        datas = reversed(list(reader))
    return datas

def append_data(filename, story, KEYS):
    values = []
    for value in story.values():
        values.append(value)
    with open(filename, "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=KEYS)
        writer.writerow(values)


