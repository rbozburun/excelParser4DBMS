#!/usr/bin/python3

import pandas as pd
from shutil import copyfile
import os
import argparse
from argparse import RawTextHelpFormatter
from time import sleep


def main():
    parser = argparse.ArgumentParser(description="XLSX and CSV parser to create a database.", formatter_class=RawTextHelpFormatter)
    parser.add_argument('-f', '--file', help="\nInput file\n\n")
    parser.add_argument('-cN', '--column_name', help="Name of the column that want to replace with IDs.\n\n")
    parser.add_argument('-o', '--output', help="Output CSV file name.\n\n")
    parser.add_argument('-t', '--file_type', help="Type of the input file. \nAvailable: {CSV, XLSX}\n")
    args = parser.parse_args()

    csv_file = args.file
    column_name = args.column_name
    output_fname = args.output
    inp_ftype = args.file_type

    # First sort the given column
    # Create a dictionary which holds the id numbers of column values. 

    # First uppercase all letters in the column then sort.
    # sample_col = ['Ankara', 'Ankara', '', 'Istanbul', 'Izmir']
    # col_dict = {
    #    '': 1, 'ANKARA': 2, 'ISTANBUL': 3, 'IZMIr':4...
    # }
    # 
    # new_col = []
    # for key in sample_col:
    #   col_id = col_dict[key.upper]
    #   new_col.add(col_id)

    if inp_ftype == "CSV" or inp_ftype == "csv":
        f = open(csv_file, 'r', encoding='utf-8-sig')
        lines = f.readlines()
        f.close()

        headers = lines[0]
        headers_splitted = headers.split(',')
        headers_splitted[-1] = headers_splitted[-1].replace('\n','')
        indexOfColumn = headers_splitted.index(column_name)

        data_lines = lines[1:]
        raw_column_values = []

        for line in data_lines:
            values = line.split(',')
            col_value = values[indexOfColumn]
            if "\n" in col_value:
                col_value = col_value.replace("\n","")
            raw_column_values.append(col_value.upper())

        col_dict = {}
        id = 2
        for raw_col in raw_column_values:
            if raw_col not in col_dict.keys():
                if raw_col == "":
                    col_dict[raw_col] = 1
                
                else:
                    col_dict[raw_col] = id
                    id += 1
        
        output_id_dict = {"Data":"ID"}
        for key in col_dict.keys():
            if key not in output_id_dict.keys():
                output_id_dict[key] = col_dict[key]
        
        #Create a new CSV file for parsed column as a ID-VALUE table.
        df_dict = pd.DataFrame.from_dict(output_id_dict, orient="index")
        df_dict.to_csv(column_name + ".csv", header=False)


        id_col = []
        for raw_col in raw_column_values:
            id_col.append(col_dict[raw_col])
        

        # Copy the input file with output filename
        copyfile(csv_file,output_fname)

        # Open output csv file and update
        df = pd.read_csv(output_fname)
        
        for idx in range(len(data_lines)):
            df.loc[idx,column_name] = id_col[idx]

        df.to_csv(output_fname, index=False)

    

    elif  inp_ftype == "XLSX" or inp_ftype == "xlsx":
        # Copy the input file with output filename
        copyfile(csv_file, "temp.xlsx")
        df_excel = pd.read_excel("temp.xlsx")
        raw_column_values = df_excel[column_name].str.upper().tolist()

        col_dict = {}
        id = 2
        for raw_col in raw_column_values:
            raw_col = str(raw_col)
            raw_col = raw_col.replace(',','/')

            if raw_col not in col_dict.keys():
                if raw_col == "nan":
                    col_dict[''] = 1
                
                else:
                    col_dict[raw_col] = id
                    id += 1
        
        output_id_dict = {"Data":"ID"}
        for key in col_dict.keys():
            if key not in output_id_dict.keys():
                output_id_dict[key] = col_dict[key]

        #Create a new CSV file for parsed column as a ID-VALUE table.
        df_dict = pd.DataFrame.from_dict(output_id_dict, orient="index")
        df_dict.to_csv(column_name + ".csv", header=False)

        id_col = []
        for raw_col in raw_column_values:
            raw_col = str(raw_col)
            raw_col = raw_col.replace(",","/")
            if raw_col == "nan":
                id_col.append(col_dict[''])

            else:
                id_col.append(col_dict[raw_col])
        
         # Open output csv file and update
        for idx in range(len(raw_column_values)):
            df_excel.loc[idx,column_name] = id_col[idx]

        df_excel.to_csv(output_fname, index=False)
        df_excel.to_excel(output_fname+".xlsx", index=False)
        

    
        os.remove("temp.xlsx")




if __name__ == "__main__":
    run = main()