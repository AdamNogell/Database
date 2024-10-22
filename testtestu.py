#! /home/adam/Desktop/PhD/Database/venv/bin/python

list = ["Iran_GanjDareh_N"]

for item in list:
    if item.endswith('_N') or '_N_' in item or '_N.' in item or '_LN' in item or '_MN' in item or '_PN' in item or 'Ceramic' in item or 'LIP' in item or 'MH' in item or 'EIP' in item:
        print("Neolithic")