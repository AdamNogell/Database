#! /home/adam/Desktop/PhD/Database/venv/bin/python

reference_url_file = '/home/adam/Desktop/PhD/Database/reference_url.csv'
data_url_file = '/home/adam/Desktop/PhD/Database/data_url.csv'
reference_url = []
data_url = []

with open(reference_url_file, 'r', encoding='utf8') as reference:
    for line in reference:
        if line != 'reference_link':
            reference_url.append(line.strip())
            
with open(data_url_file, 'r', encoding='utf8') as data:
    for line in data:
        if line != 'data_link':
            data_url.append(line.strip())
            
print(data_url[10:20])