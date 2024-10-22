#! /home/linuxbrew/.linuxbrew/bin/python3

import re

def separate(input_list):
    output_list = []
    for i in input_list:
        separated_word = re.sub(r'([A-Z])', r' \1', i).strip()
        separated_word = separated_word.replace('2', ' 2', 1)
        output_list.append(separated_word)
    return output_list

input_list = []

with open("AARD_noAmtDB_pub_sort.txt", 'r') as txt:
    for line in txt:
        input_list.append(line.strip())

output_list = separate(input_list)

with open("test.txt", 'w') as txtout:
    for i in output_list:
        txtout.write(f"{i}\n")
        