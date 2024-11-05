#! /home/adam/Desktop/PhD/Database/venv/bin/python

from convert_func import convert
import time

start_time = time.time()

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

    continent = convert.continent_extract(df, input_dict)
    epoch = convert.epoch_extract(df)
    year_start, year_end, bp, c14 = convert.parse_years(df)
    publications, urls = convert.pub_url(df)
    try:
        convert.reorganize_csv(df, output_file, continent, epoch, year_start, year_end, bp, c14, publications, urls)
    except:
        print("Something failed")
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Run time: {run_time:.2f} seconds")
        print("continent:", len(continent))
        print("epoch:", len(epoch))
        print("year_start:", len(year_start))
        print("year_end:", len(year_end))
        print("bp:", len(bp))
        print("c14_lab_code:", len(c14))
        print("publications:", len(publications))
        print("urls:", len(urls))
        print("identifier:", len(df.iloc[:, 1]))
        print("country:", len(df.iloc[:, 13]))
        print("region:", len(df.iloc[:, 12]))
        print("culture:", len(df.iloc[:, 11]))
        print("latitude:", len(df.iloc[:, 14]))
        print("longitude:", len(df.iloc[:, 15]))
        print("sex:", len(df.iloc[:, 22]))
        print("site:", len(df.iloc[:, 11]))
        print("mt_hg:", len(df.iloc[:, 27]))
        print("ychr_hg:", len(df.iloc[:, 25]))
        print("date_detail:", len(df.iloc[:, 9]))
        print("avg_coverage:", len(df.iloc[:, 19]))
        print("sequence_source:", len(df.iloc[:,17]))
    
end_time = time.time()
run_time = end_time - start_time
print(f"Run time: {run_time:.2f} seconds")