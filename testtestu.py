#! /home/adam/Desktop/PhD/Database/venv/bin/python

import pyperclip

list = ["4500-3500 BCE"]
    
year = []

for item in list:
        index = item.find('CE')
        if index != -1:
            cropped_item = item[:(index+2)]
            year.append(cropped_item)
        else:
            year.append(item)
                
for item in year:
    years = item.split('-')
    year1 = years[0]
    year2 = years[1].strip(' BCE')
print(f"years = {years}\nyear1 = {year1}\nyear2 = {year2}")