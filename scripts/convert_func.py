#!/home/adam/Desktop/PhD/Database/venv/bin/python

import pandas as pd
import re, requests, urllib.parse
from bs4 import BeautifulSoup

class convert:
    def continent_extract(df):

        '''
        Extract continent from column 14 of the data frame according to the country in the column.
        '''

        column_14 = df.iloc[:, 13]
        continent = []
        geo_group = []
        
        input_dict = {
        "Africa": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde","Cameroon", "CAR", "Central African Republic", "Chad", "Comoros", "Congo", "Democratic Republic of the Congo", "Djibouti", "DRC", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"],
        "Asia": ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "UAE", "Uzbekistan", "Vietnam", "Yemen"],
        "Europe": ["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Channel Islands", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Isle of Man" "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom", "UK", "England", "Scotland", "Northern Ireland", "Vatican City", "Vatican"],
        "North America": ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", "Curacao" "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Puerto Rico", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States", "United States of America", "USA", "US"],
        "South America": ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"],
        "Oceania": ["Australia", "Federated States of Micronesia", "Fiji", "Guam" "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]
        }

        for item in column_14:
            if item in input_dict["Africa"]:
                continent.append("Africa")
            elif item in input_dict["Asia"]:
                continent.append("Asia")
            elif item in input_dict["Europe"]:
                continent.append("Europe")
            elif item in input_dict["North America"]:
                continent.append("North America")
            elif item in input_dict["South America"]:
                continent.append("South America")
            elif item in input_dict["Oceania"]:
                continent.append("Oceania")
            else:
                continent.append(item)

        for item in column_14:
            if ('Turkey' in item):
                geo_group.append("Anatolia")
            elif ('United Kingdom' in item or 'Channel Islands' in item or 'Isle of Man' in item or 'Ireland' in item):
                geo_group.append("British Isles")
            elif ('Bahamas' in item or 'Belize' in item or 'Dominican Republic' in item or 'Curacao' in item or 'Haiti' in item or 'Puerto Rico' in item):
                geo_group.append("Caribbean")
            elif ('Guam' in item or 'Micronesia' in item or 'Vanuatu' in item):
                geo_group.append("Oceania")
            elif ('Spain' in item or 'Portugal' in item):
                geo_group.append("Iberia")
            elif ('Armenia' in item or 'Azerbaijan' in item or 'Georgia' in item):
                geo_group.append("Caucasus")
            elif ('Albania' in item or 'Bulgaria' in item or 'Bosnia' in item or 'Serbia' in item or 'Montenegro' in item or 'Kosovo' in item or 'Macedonia' in item or 'Greece' in item or 'Croatia' in item or 'Slovenia' in item or 'Romania' in item):
                geo_group.append("Balkans")
            elif ('Estonia' in item or 'Lithuania' in item or 'Latvia' in item):
                geo_group.append("Baltic")
            elif ('Egypt' in item or 'Israel' in item or 'Iraq' in item or 'Jordan' in item or 'Palestine' in item or 'Syria' in item or 'Saudi Arabia' in item or 'Qatar' in item or 'Bahrain' in item or 'Kuwait' in item or 'UAE' in item or 'Emirates' in item or 'Oman' in item or 'Yemen' in item or 'Lebanon' in item):
                geo_group.append("Near East")
            elif ('Iran' in item or 'Afghanistan' in item or 'Pakistan' in item):
                geo_group.append("Middle East")
            elif ('Norway' in item or 'Sweden' in item or 'Denmark' in item or 'Finland' in item or 'Iceland' in item):
                geo_group.append("Scandinavia")
            elif ('Moldova' in item or 'Ukraine' in item):
                geo_group.append("Pontic steppe")
            elif ('Austria' in item or 'Czech' in item or 'Slovak' in item or 'Germany' in item or 'Switzerland' in item or 'Hungary' in item or 'Poland' in item or 'Liechtenstein' in item):
                geo_group.append("central Europe")
            elif ('France' in item or 'Netherlands' in item or 'Belgium' in item or 'Luxembourg' in item):
                geo_group.append("western Europe")
            elif ('Italy' in item):
                geo_group.append("southern Europe")
            elif ('Sudan' in item or 'Ethiopia' in item or 'Kenya' in item or 'Malawi' in item or 'Zambia' in item or 'Tanzania' in item):
                geo_group.append("eastern Africa")
            elif ('Japan' in item or 'China' in item or 'Taiwan' in item or 'Mongolia' in item or 'Myanmar' in item or 'Thailand' in item or 'Vietnam' in item):
                geo_group.append("east Asia")
            elif ('Uzbekistan' in item or 'Tajikistan' in item or 'Turkmenistan' in item or 'Kyrgyzstan' in item or 'Kazakhstan' in item):
                geo_group.append("central Asia")
            elif ('Chile' in item or 'Argentina' in item):
                geo_group.append("Patagonia")
            elif ('Bolivia' in item or 'Mexico' in item or 'Brazil' in item or 'Peru' in item or 'Uruguay' in item or 'Paraguay' in item or 'Suriname' in item or 'Guyana' in item or 'Venezuela' in item or 'Ecuador' in item or 'Colombia' in item or 'Honduras' in item or 'Nicaragua' in item or 'El Salvador' in item or 'Guatemala' in item):
                geo_group.append("Latin America")
            elif ('Cameroon' in item):
                geo_group.append("central Africa")
            elif ('South Africa' in item):
                geo_group.append("south Africa")
            else:
                geo_group.append(item)

        return continent, geo_group
    
    def epoch_extract(df):

        '''
        Extract archaeological epochs from column 12 of the data frame.
        '''

        column_12 = df.iloc[:, 11]
        epoch = []
        group = []

        for item in column_12:
            if (item.endswith('_HG') or '_HG_' in item or 'LSA' in item):
                epoch.append("Paleolithic")
            elif ('Mesolithic' in item or 'Natufian' in item):
                epoch.append("Mesolithic")
            elif (item.endswith('_N') or '_N_' in item or '_N.' in item or '_LN' in item or '_EN' in item or '_MN' in item or '_PN' in item or 'Ceramic' in item or 'LIP' in item or 'MH' in item or 'EIP' in item or 'Yamana' in item):
                epoch.append("Neolithic")
            elif (item.endswith('_C') or '_C_' in item):
                epoch.append("Copper Age")
            elif (item.endswith('_H') or '_H_' in item or 'MLBA' in item or 'MBA' in item or 'EBA' in item or 'LBA' in item or 'IBA' in item or 'BA' in item or 'BellBeaker' in item):
                epoch.append("Bronze Age")
            elif ('MLIA' in item or 'MIA' in item or 'EIA' in item or 'LIA' in item or 'IIA' in item or 'IA' in item or 'Roopkund' in item or 'Antiquity' in item or 'EarlyChristian' in item or 'Archaic' in item):
                epoch.append("Iron Age")
            elif ('Avar' in item or 'SMA' in item or 'Medieval' in item or 'Byzantine' in item or 'Latte' in item):
                epoch.append("Middle Age")
            elif ('Modern' in item):
                epoch.append("Modern Era")
            else:
                epoch.append('')
                
        for item in column_12:
            if (item.endswith('_HG') or '_HG_' in item or 'LSA' in item):
                group.append("PAXX")
            elif ('Mesolithic' in item or 'Natufian' in item):
                group.append("MEXX")
            elif (item.endswith('_N') or '_N_' in item or '_N.' in item or '_EN' in item or '_MN' in item or '_PN' in item or 'Ceramic' in item or 'LIP' in item or 'MH' in item or 'EIP' in item or 'Yamana' in item):
                group.append("NEXX")
            elif (item.endswith('_LN') or '_LN' in item or '_LN.' in item):
                group.append("LNEXX")
            elif (item.endswith('_C') or '_C_' in item):
                group.append("CAXX")
            elif (item.endswith('_H') or '_H_' in item or 'MLBA' in item or 'MBA' in item or 'EBA' in item or 'LBA' in item or 'IBA' in item or 'BA' in item or 'BellBeaker' in item):
                group.append("BAXX")
            elif ('EBA' in item):
                group.append("EBAXX")
            elif ('MLIA' in item or 'MIA' in item or 'EIA' in item or 'LIA' in item or 'IIA' in item or 'IA' in item or 'Roopkund' in item or 'Antiquity' in item or 'EarlyChristian' in item or 'Archaic' in item):
                group.append("IAXX")
            elif ('Avar' in item or 'SMA' in item or 'Medieval' in item or 'Byzantine' in item or 'Latte' in item):
                group.append("MAXX")
            else:
                group.append('')
        
        return epoch, group

    def parse_years(df):

        '''
        Extract year range from column 10 of the data frame.
        '''

        column_10 = df.iloc[:, 9]
        year_start = []
        year_end = []
        bp = []
        c14 = []
        tag = []

        for item in column_10:
            match1 = re.match(r'"*(\d+)\s+(\w+)\s*-\s*(\d+)\s+(\w+)', item)
            match2 = re.match(r'"*(\d+)\s*-\s*(\d+)\s+(\w+)', item)
            if match1:
                number1, string1, number2, string2 = match1.groups()
                if "BCE" in string1:
                    year1 = f"-{number1}"
                elif "CE" in string1:
                    year1 = f"{number1}"
                if "BCE" in string2:
                    year2 = f"-{number2}"
                elif "CE" in string2:
                    year2 = f"{number2}"
                else:    
                    year1 = f"{number1} {string1}"
                    year2 = f"{number2} {string2}"
            elif match2:
                number1, number2, string1 = match2.groups()
                if "BCE" in string1:
                    year1 = f"-{number1}"
                    year2 = f"-{number2}"
                elif "CE"in string1:
                    year1 = f"{number1}"
                    year2 = f"{number2}"
                else:
                    year1 = f"{number1} {string1}"
                    year2 = f"{number2} {string1}"
            else:
                year1 = item
                year2 = item
            year_start.append(year1)
            year_end.append(year2)

        for item in column_10:
            try:
                if '(' in item:
                    extract = item.split("(")
                    extract[-1] = extract[-1].strip('")]')
                    if ',' in extract[-1]:
                        bp_value, c14_value = extract[-1].split(',')
                        bp.append(bp_value.strip())
                        c14.append(c14_value.strip())
                    else:
                        bp_value = extract[-1].split('BP')[0] + 'BP'
                        c14_value = extract[-1].split('BP')[1].strip()
                        bp.append(bp_value)
                        c14.append(c14_value)
                else:
                    bp.append('')
                    c14.append('')
            except: 
                bp.append('')
                c14.append('')
        
        for item in column_10:
            if 'cal' in item:
                tag.append(1)
            else:
                tag.append(0)
            
        return year_start, year_end, bp, c14, tag

    def pub_url(df):

        '''
        Insert spaces in the publication data from column 6 of the data frame and use it to retrieve URL of the publication according to Google Scholar (URL retrieval currently paused).
        '''

        column_6 = df.iloc[:, 5]
        publications = []
        urls = []
        
        for item in column_6:
            spaced_pub = re.sub(r'([A-Z])', r' \1', item).strip().replace('2', ' 2', 1)
            short_pub, year_pub = spaced_pub.split(' ', 1)[0], spaced_pub.split(' ')[-1]
            pub = f"{short_pub} et al. {year_pub}" 
            publications.append(pub)
            #query = urllib.parse.quote_plus(spaced_pub)
            #url = f"https://scholar.google.com/scholar?q={query}"
            #headers = {
            #    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
            #}
            #response = requests.get(url, headers=headers)
            #if response.status_code == 200:
            #    soup = BeautifulSoup(response.text, 'html.parser')
            #    first_result = soup.find('h3', class_='gs_rt')
            #    if first_result:
            #        link = first_result.find('a')
            #        if link and 'href' in link.attrs:
            #            paper_url = link['href']
            #            urls.append(paper_url)
            #        else:
            #            urls.append('none')
            #    else:
            #        urls.append('none')
            #else:
            #    urls.append('none')
            #urls.append('TBA')
        return publications

    def reorganize_csv(df, output_file, continent, epoch, year_start, year_end, bp, c14, publications, reference_url, data_url, geo_group, group, tag):   

        '''
        Reorganize CSV file in the AADR format into a CSV file in the AmtDB format.
        '''

        reorganized_df = pd.DataFrame({
            "id": df.iloc[:, 1],
            "id_alt": '',
            "country": df.iloc[:, 13],
            "continent": continent,
            "geo_group": geo_group,
            "culture": df.iloc[:, 11],
            "epoch": epoch,
            "group": group,
            "comment": df.iloc[:, 12],
            "latitude": df.iloc[:, 14],
            "longitude": df.iloc[:, 15],
            "sex": df.iloc[:, 22],
            "site": df.iloc[:, 11],
            "site_detail": '',
            "mt_hg": df.iloc[:, 27],
            "ychr_hg": df.iloc[:, 25],
            "ychr_snps":'',
            "year_from": year_start,
            "year_to": year_end,
            "date_detail": df.iloc[:, 9],
            "bp": bp,
            "c14_lab_code": c14,
            "reference_name": publications,
            "reference_link": reference_url,
            "data_link": data_url,
            "c14_sample_tag":tag,
            "c14_layer_tag": '',
            "full_mt_tag":'',
            "trusted_tag":'',
            "avg_coverage": df.iloc[:, 19],
            "amtdb_version": 'v1.010'
        })

        reorganized_df.to_csv(output_file, sep=';', index=False) 
