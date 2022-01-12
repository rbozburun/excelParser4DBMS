
# XLSX and CSV Parser

Parse your CSV or XLSX files to create a database. 
This script allows you create seperate relational tables. You can create ID's for your columns.

For example, you have a Students table:

| Student_ID   |      Student_Name      |  City |
|----------|:-------------:|------:|
|11 |  John | London |
| 12 |    Alice   |   Los Angles |
| 13 | Jessy |    London |
| 14 | Jeff |    London |
| 15 | Samuel |    Washington |


To create an relational database, you want to create a new City table:

| City_ID   |  City |
|----------|------:|
|1 |  London |
| 2 |    Los Angles |
| 3 |     Washington |


You can use the script to achieve this. 

## Usage


```plaintext
python3 parse_excel.py -f students_all.xlsx -cN City -o city.csv -t xlsx
```
This command will create:
- City.csv file which holds City_ID and City columns.
- city.csv file which converted City column values to their IDs.
- city.csv.xlsx file which converted City column values to their IDs.


```plaintext
python3 v2_parsePerson2Drug.py excel_file
```
This command will create a new excel file. This excel file contains Personality_IDs for each column except Personality_ID column. Let assume that you have a table:

| Personality_ID   |      Opt1     |  Opt2 |
|----------|:-------------:|------:|
|11 |  Y | Y |
| 12 |    Y   |    |
| 13 |  |    Y |

Script reates a new table like that:
| Personality_ID   |      Drug_ID     |
|----------|:-------------:|
|11 |  1 |
| 11 |    2   |  
| 12 |   1   |  
| 13 |    2   |  


