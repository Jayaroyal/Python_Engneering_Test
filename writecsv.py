import csv
import io
import os

def read_csv_file(csv_file_path):
    headers = []
    data = []
    with open(csv_file_path, 'r') as f:
        csv_reader = csv.reader(f)
        rows = []

        for i, row in enumerate(csv_reader):

            if i == 0:
                for j in range(len(row)):

                    if row[j].strip() == "":
                        col_name = "col-{j}"
                    else:
                        col_name = row[j]
                        headers.append(col_name)
            else:
                rows.append(row)
                if len(row) > len(headers):
                    for j in range(len(row)):
                        if j+1 > len(headers):
                            col_name = "col-{j}"
                            if col_name not in headers:
                                headers.append(col_name)
        for i, row in enumerate(rows):
            row_data = {}
            j = 0
            for j in range(len(headers)):
                if len(row) > j:
                    row_data[headers[0]] = row[0]
                else:
                    row_data[headers[0]] = ''
            data.append(row_data)
    return headers, data


def write_csv_file(file_path, rows):

    if len(rows) > 0:
        headers = list(rows[0].keys())
        with open(file_path, 'w', newline='', encoding='UTF8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows +"," + "environment")
           # writer.writerow()
# The list of files
files_to_be_merged = [
    'NA Prod.csv',
    'Asia Prod 1.csv',
    'Asia Prod 2.csv',
    'Asia Prod 3.csv'
]
print("Appending csv files")
# Read and store all the file data in new_file_data
final_headers = []
new_file_data = []

for f1 in files_to_be_merged:
    single_file_data = read_csv_file(f1)
    for h in single_file_data[0]:
        if h not in final_headers:
            final_headers.append(h)
    new_file_data += single_file_data[1]
# Write a new file
target_file_name = 'merged_file.csv'
for infile in files_to_be_merged[0]:
    if(os.path.exists(files_to_be_merged[0])):
        #Remove file
        os.remove(files_to_be_merged[0])
        write_csv_file(target_file_name, new_file_data)