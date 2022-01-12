
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


To create an acctive database, you want to create a new City table:

| City_ID   |  City |
|----------|------:|
|1 |  London |
| 2 |    Los Angles |
| 3 |     Washington |


You can use the script to achieve this. 


```plaintext
python3 parse_excel.py -f students_all.xlsx -cN City -o city.csv -t xlsx
```
Below command will create:
- City.csv file which holds City_ID and City columns.
- city.csv file which converted City column values to their IDs.
- city.csv.xlsx file which converted City column values to their IDs.


