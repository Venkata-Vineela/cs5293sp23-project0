import argparse
import requests
import re
import PyPDF2
import sqlite3
def fetch(url):
    response = requests.get(url)
    if response.status_code == 200:
        print('Fetch Successful')
        with open('incident.pdf', 'wb') as f:
            f.write(response.content)
    else:
        print('Fetch Failed')
    return 'incident.pdf'
def extract(incident_data_file):
   with open(incident_data_file, 'rb') as f:
        data=[]
        pdf = PyPDF2.PdfReader(f)
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            page_text = page.extract_text()
            for line in page_text.split('\n'):
                pattern = r'^(\d{1,2}/\d{1,2}/\d{4})\s+(\d{1,2}:\d{2})\s+(\d{4}-\d{8})\s+(.*)\s+(\w+)$'
                match = re.match(pattern, line)
                if match:
                    incident_date = match.group(1)
                    incident_time = match.group(2)
                    incident_number = match.group(3)
                    address = match.group(4)
                    ori_number = match.group(5)
                    words = address.split(' ')
                    nature=' '
                    lowercase_found = False
                    for word in words:
                      if not lowercase_found and any(c.islower() for c in word):
                            lowercase_found = True
                      if lowercase_found:
                            nature += word + ' '
                            address = address.replace(word, '', 1)
                    line_list=[incident_date,incident_time,incident_number,address,nature,ori_number]
                    data.append(line_list)
        return data
def database(data):
    x=sqlite3.connect('database.db')
    y=x.cursor()
    y.execute('DROP TABLE IF EXISTS Incident_table')
    y.execute('''CREATE TABLE Incident_table (date TEXT, time TEXT, incident_number TEXT, address TEXT, nature TEXT, ORI_number TEXT)''')
    for i in data:
        y.execute('INSERT INTO Incident_table (date, time, incident_number, address, nature, ORI_number) VALUES (?, ?, ?, ?, ?, ?)', i)
    y.execute('SELECT nature, COUNT(*) FROM Incident_table GROUP BY nature')
    op=y.fetchall()
    for row in op:
        print(row[0],'|',row[1])
    x.commit()

