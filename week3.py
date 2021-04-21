import csv
def read_csv_fieldnames(filename, separator, quote):
  with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,delimiter=separator,quotechar=quote, quoting=csv.QUOTE_MINIMAL)
  return csvreader.fieldnames
 
def read_csv_as_list_dict(filename, separator, quote):
    table = []
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator,quotechar=quote, quoting=csv.QUOTE_MINIMAL)
        for row in csvreader:
            table.append(row)
    return table

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    table = {}
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote, quoting=csv.QUOTE_MINIMAL)
        for row in csvreader:
            table[row[keyfield]] = row
    return table


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
  with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile,fieldnames=fieldnames, delimiter=separator,quotechar=quote,quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        for row in table:
            csv_writer.writerow(row)
