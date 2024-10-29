#! /home/adam/Desktop/PhD/Database/venv/bin/python

column_10 = ['100 BCE - 300 CE', '1447-1621 calCE (390±20 BP PSUAMS-11907)', '"4227-3965 calBCE (5270±25 BP, UCIAMS-186346)"', '141-1631 calCE (428±46 BP) [R_combine: union of two dates: (B-4996); (B-5006)]']

bp = []
c14 = []
for item in column_10:
    try:
        if '(' in item:
            extract = item.split("(")
            extract[-1] = extract[-1].strip('")]')
            if ',' in extract[-1]:
                bp.append(extract[-1].split(',')[0])
                c14.append(extract[-1].split(',')[1].strip(" "))
            else:
                bp.append(extract[-1].split('BP')[0]+'BP')
                c14.append(extract[-1].split('BP')[1].strip(" "))
        else:
            bp.append('none')
            c14.append('none')
    except: 
        bp.append('none')
        c14.append('none')

print(bp)
print(c14)
