import os
from project0.func import fetch, extract, database
import sqlite3
import pytest

url= 'https://www.normanok.gov/sites/default/files/documents/2023-01/2023-01-01_daily_incident_summary.pdf'

def test_fetch():
    file=fetch(url)
    assert file == 'incident.pdf'
    assert os.path.exists('incident.pdf')==True
    os.remove('incident.pdf')

def test_extract():
    incident_file=fetch(url)
    data = extract(incident_file)
    assert data[0][0] == '1/1/2023'

def test_database():
    data=[['1/1/2023', '0:06', '2023-00000001', '2000 ANN BRANDEN BLVD', 'Transfer/Interfacility', 'EMSSTAT'], ['1/1/2023', '0:15', '2023-00000001', '1432 24TH AVE SE', 'Fireworks', 'OK0140200']]
    database(data)
    conn=sqlite3.connect('database.db')
    cur=conn.cursor()
    cur.execute('SELECT DISTINCT date FROM Incident_table')
    testresult=[row[0] for row in cur.fetchall()]
    assert testresult == ['1/1/2023']

if __name__ == '__main__':
    test_fetch()
    test_extract()
    test_database()
