#! /home/adam/Desktop/PhD/Database/venv/bin/python

import csv

# Input files
grepsort_file = '/home/adam/Desktop/PhD/Database/temp/sorted.csv'
metadata_file = '/home/adam/Desktop/PhD/Database/output/converted_metadata.csv'
output_file = '/home/adam/Desktop/PhD/Database/output/modified_metadata.csv'

# Function to determine if the string is type A or B
def determine_type(string):
    if ('NakatsukaCell2020' in string or 'LipsonCurrentBiology2020' in string or 'LipsonCurrentBiology2018' in string or 'FernandesNatureEcologyEvolution2020' in string):
        return 'A'
    else:
        return 'B'

# Read 'grepsort.csv' and store ID-to-type mapping
id_type_mapping = {}
with open(grepsort_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if len(row) >= 2:
            id_type_mapping[row[0]] = determine_type(row[1])

# Process 'converted_metadata.csv' and modify column 23 based on the mapping
with open(metadata_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter=';')
    writer = csv.writer(outfile, delimiter=';')

    for row in reader:
        if len(row) >= 23:
            id_ = row[0]
            if id_ in id_type_mapping:
                string_type = id_type_mapping[id_]
                row[22] += f" ({string_type})"
        writer.writerow(row)

print(f"Modified file has been saved as '{output_file}'")
