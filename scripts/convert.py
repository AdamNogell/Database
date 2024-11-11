#! /home/adam/Desktop/PhD/Database/venv/bin/python

from convert_func import convert
import time
import pandas as pd

start_time = time.time()
input_file = '../AADR_data/metadata_for_sequences_not_present_in_AmtDB_geneticID.csv'
df = pd.read_csv(input_file)
output_file = '../converted_metadata.csv'

if __name__ == "__main__":
    continent = convert.continent_extract(df)
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