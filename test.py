#! /home/adam/Desktop/PhD/Database/venv/bin/python

import pyperclip

input_file = 'test.csv'

with open(input_file, 'r', encoding='utf-8') as infile:
    
    year = []
    
    for idx, item in enumerate(infile):
        if idx != 0:
    
            index = item.find('CE')
            if index != -1:
                cropped_item = item[:(index+2)]
                year.append(cropped_item)
            else:
                year.append(item)
                
for item in year:
    item.split()
pyperclip.copy(year)