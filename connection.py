import csv


def read_data(filename):
    with open(filename, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        datas = list(reader)
    return datas

def append_data(filename, story, KEYS):
    with open(filename, "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=KEYS)
        writer.writerow(story)

def write_data(filename, fieldnames, datas):
    with open(filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for data in datas:
            writer.writerow(data)