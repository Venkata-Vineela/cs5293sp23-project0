

# cs5293sp23-project0
Name: Venkata Vineela Kanamarlapudi

## Description:

This project involves downloading an incident PDF file from the Norman Police Department website that contains summaries of three types: arrests, cases, and incidents reports from the Norman area. Once the file is downloaded, it is then processed using Python in order to extract the data from the PDF. The data is then stored in SQLite Database to retrieve the unique nature of incidents and their occurrences in the Norman.

Python, Linux commands, GIT and SQLite3 are used in this project.

## Packages Used:
- urllib
- argparse
- requests
- re
- PyPDF2
- SQLite3
- Os
- pytest

## Structure:
![Screenshot 2023-03-07 203127](https://user-images.githubusercontent.com/124094317/223608268-4a460203-dc5d-4742-b273-252368368850.png)

## Installation Procedure:
- Create directory: *mkdir my_project*.
- Change the path to the newly created directory: *cd my_project*
- Download the project file from git: *git clone https://github.com/Venkata-Vineela/cs5293sp23-project0*
- Navigate to the downloaded project directory: *cd project cs5293sp23-project0* 
- Install pipenv using the following command: *pip install pipenv*
- Create a Python3 virtual environment: *pipenv –python 3*
- Install the required packages for the project using the command: *pip install <packagename>*

## Execution:
- The project0 folder contains two python files: main.py and func.py. To execute the main code, we use the below command:
 *pipenv run python3 project0/main.py –incidents <paste the url here>*
- And to run the test cases, the following command is used:
 *pipenv run python -m pytest*

## External Resources:
- https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/
- https://www.programiz.com/python-programming/regex
- https://docs.python.org/3.10/library/sqlite3.html
    
## Assumptions:
- The code works only on PDF files that follow a specific format as used by the Oklahoma Police department website.
- The code has limitations in handling PDF files that have multi-line data, as it is designed to assume that each line of text as a single incident record. 
- The code is built in a way that it operates on non-NULL fields. It might result in inappropriate output when NULL values are present.
    
## Methods Used:
In the project0 folder, there are two python files ‘main.py’ and ‘func.py.
In func.py, the following functions are defined and are being called by the main.py.
    
#### fetch()
- The function takes an argument ‘url’ which is the url of the resource to fetch.
- It uses requests lib to fetch the content of the resource
- If the response status code is 200(i.e, successful response), the function prints ‘Fetch Successful’ and writes the content of the response to a file name ‘incident.pdf’.
- If the response status code is not 200, it prints ‘Fetch Failed’.
- Finally, it returns the filename ‘incident.pdf’.
    
#### extract():
The extract() method takes a PDF file as an input and extracts incident report data from it.
- This function initially opens the PDF file using the ‘rb’ mode, and reads the data from the PDF file using PyPDF2 library.
- Then it iterates through each page and uses the ‘extract_text’ method to extract the text and splits the text in each page using ‘\n’ character as the separator.
- Each line that contains incident report data is classified into different fields using regular expression patterns.
- The fields that are extracted are appended into the list. 
- This process continues for every page of the PDF file until all incident data has been extracted.
- Finally, the function returns the extracted incident data as a list of lists, where each sub list contains the incident data for a single incident report.
    
#### database():
The database() method takes an argument as a list and stores each tuple as a row in the database.
- The function uses the sqlite3 module in Python to create the database.
- It starts by connecting to the database and creating a cursor object using connect() and cursor() methods respectively.
- Then the ‘incident_table’ is created and each item of the list is inserted into the table.
- The statement – ‘SELECT nature, COUNT(*) FROM Incident_table GROUP BY nature’ counts the number of incidents for each nature using the GROUP BY clause.
- The results are then fetched using the fetchall() method and then they are printed using the ‘for loop’ that iterates through each row of the result set.
    
## Project0/test.py
Pytest is a framework available in python which provides a simple way to define and run test functions in python.
    
#### test_fetch():
The test_fetch() method is used to verify if the fetch() method is able to download a PDF file from a given URL, and if the downloaded file exists and can be subsequently deleted.
    
#### test_extract():
The test_extract() method is used to verify whether the extract() method is able to extract incident data correctly from a downloaded PDF file, by checking the value of the first incident record’s date field.
    
#### test_database():
The test_database() method is used to check if the data insertion into the database was successful or not by connecting to the database and executing an SQL statement to count the number of rows in the ‘Incident_table’.
    
## Database Develeopment:
The database() method which is defined in the func.py and invoked by the main.py, is used to create a database to store the incident records. Within this database, we create a table called ‘Incident_data’ to insert the records.
    
To create a table, we use:
CREATE TEABLE Incident_table (date TEXT, time TEXT, incident_nature TEXT, address TEXT, nature TEXT, ORI_number TEXT)

