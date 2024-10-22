#! /home/adam/Desktop/PhD/Database/venv/bin/python

import pandas as pd

def continent_extract(df, input_dict):
    column_14 = df.iloc[:, 13]

    continent = []
    
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
    
    return continent

def epoch_extract(df):
    column_12 = df.iloc[:, 11]

    epoch = []
    
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
        elif ('MLIA' in item or 'MIA' in item or 'EIA' in item or 'LIA' in item or 'IIA' in item or 'IA' in item or 'Roopkund' in item):
            epoch.append("Iron Age")
        elif ('Antiquity' in item or 'EarlyChristian' in item or 'Archaic' in item or 'Inca' in item):
            epoch.append("Classical Age")
        elif ('Avar' in item or 'SMA' in item or 'Medieval' in item or 'Byzantine' in item or 'Latte' in item):
            epoch.append("Middle Age")
        elif ('Modern' in item):
            epoch.append("Modern Era")
    return epoch

def reorganize_csv(df, output_file, continent, epoch):   
    reorganized_df = pd.DataFrame({
        "identifier": df.iloc[:, 1],
        "alternative_identifiers": 'none',
        "country": df.iloc[:, 13],
        "continent": continent,
        "region": df.iloc[:, 12],
        "culture": df.iloc[:, 11],
        "epoch": epoch,
        "group": 'none',
        "comment": 'none',
        "latitude": df.iloc[:, 14],
        "longitude": df.iloc[:, 15],
        "sex": df.iloc[:, 22],
        "site": df.iloc[:, 11],
        "site_detail": "none",
        "mt_hg": df.iloc[:, 27],
        "ychr_hg": df.iloc[:, 25],
        "year_from": "",
        "year_to": "",
        "date_detail": "",
        "bp": "",
        "c14_lab_code": "",
        "reference_name": "",
        "reference_link": "",
        "data_link": "",
        "c14_sample_tag": "",
        "c14_layer_tag": "",
        "ychr_snps": "",
        "avg_coverage": "",
        "sequence_source": "",
        "mitopatho_alleles": "",
        "mitopatho_positions": "",
        "mitopatho_locus": "",
        "mitopatho_diseases": "",
        "mitopatho_statuses": "",
        "mitopatho_homoplasms": "",
        "mitopatho_heteroplasms": "",
    })
    
    reorganized_df.to_csv(output_file, index=False) 

if __name__ == "__main__":
    input_file = 'metadata_for_sequences_not_present_in_AmtDB_geneticID.csv'
    df = pd.read_csv(input_file)
    output_file = 'converted_metadata.csv'
    input_dict = {
        "Africa": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde","Cameroon", "CAR", "Central African Republic", "Chad", "Comoros", "Congo", "Democratic Republic of the Congo", "Djibouti", "DRC", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"],
        "Asia": ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "UAE", "Uzbekistan", "Vietnam", "Yemen"],
        "Europe": ["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom", "UK", "England", "Scotland", "Northern Ireland", "Vatican City", "Vatican"],
        "North America": ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States", "United States of America", "USA", "US"],
        "South America": ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"],
        "Oceania": ["Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]
    }

    continent = continent_extract(df, input_dict)
    epoch = epoch_extract(df)
    reorganize_csv(df, output_file, continent, epoch)
