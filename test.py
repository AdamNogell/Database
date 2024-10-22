#! /home/adam/Desktop/PhD/Database/venv/bin/python

import pyperclip

input_file = 'test.csv'

with open(input_file, 'r', encoding='utf-8') as infile:
    epoch = []
    for line in infile:
        line = line.strip()
        if (line.endswith('_HG') or '_HG_' in line or 'LSA' in line):
            epoch.append("Paleolithic")
        elif 'Mesolithic' in line:
            epoch.append("Mesolithic")
        elif (line.endswith('_N') or '_N_' in line or '_N.' in line or '_LN' in line or '_MN' in line or '_PN' in line or 'Ceramic' in line or 'LIP' in line or 'MH' in line or 'EIP' in line):
            epoch.append("Neolithic")
        elif (line.endswith('_C') or '_C_' in line):
            epoch.append("Copper Age")
        elif (line.endswith('_H') or '_H_' in line or 'MLBA' in line or 'MBA' in line or 'EBA' in line or 'LBA' in line or 'IBA' in line or 'BA' in line or 'BellBeaker' in line):
            epoch.append("Bronze Age")
        elif ('MLIA' in line or 'MIA' in line or 'EIA' in line or 'LIA' in line or 'IIA' in line or 'IA' in line):
            epoch.append("Iron Age")
        elif ('Antiquity' in line or 'EarlyChristian' in line or 'Archaic' in line):
            epoch.append("Classical Age")
        elif ('Avar' in line or 'SMA' in line or 'Medieval' in line or 'Byzantine' in line or 'Latte' in line):
            epoch.append("Middle Age")
        elif 'Modern' in line:
            epoch.append("Modern Era")
        else:
            epoch.append(line.strip())
                
pyperclip.copy(epoch)