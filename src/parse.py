import requests
import sqlite3 as sql
from datetime import datetime

# convert regular time format to seconds
dtn = datetime.now()
dtn = dtn.replace(microsecond=0)
today = datetime.strptime(str(dtn), "%Y-%m-%d %H:%M:%S")
start = datetime(1970, 1, 1)

# calculate amount of seconds from 1970 year for nowadays
date = int((today - start).total_seconds())

# Companies which raise in rest api implementation
companies = {
    "PD": f"https://query1.finance.yahoo.com/v7/finance/download/PD?period1=1554940800&period2={date}&interval=1d&events=history&includeAdjustedClose=true",
    "ZUO": f"https://query1.finance.yahoo.com/v7/finance/download/ZUO?period1=1523491200&period2={date}&interval=1d&events=history&includeAdjustedClose=true",
    "PINS": f"https://query1.finance.yahoo.com/v7/finance/download/PINS?period1=1555545600&period2={date}&interval=1d&events=history&includeAdjustedClose=true",
    "ZM": f"https://query1.finance.yahoo.com/v7/finance/download/ZM?period1=1555545600&period2={date}&interval=1d&events=history&includeAdjustedClose=true",
    "DOCU": f"https://query1.finance.yahoo.com/v7/finance/download/DOCU?period1=1524787200&period2={date}&interval=1d&events=history&includeAdjustedClose=true",
    "CLDR": f"https://query1.finance.yahoo.com/v7/finance/download/CLDR?period1=1493337600&period2={date}&interval=1d&events=history&includeAdjustedClose=true",
    "RUN": f"https://query1.finance.yahoo.com/v7/finance/download/RUN?period1=1438732800&period2={date}&interval=1d&events=history&includeAdjustedClose=true",
}

# Web-site URL and Headers
URL = "https://query1.finance.yahoo.com/v7/finance/download/"
HEADERS = {
    "accept": "text/javascript, application/json, text/html, application/xml, text/xml, */*",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
}

# connecting and creating sqlite3 database
connect = sql.connect("data/finance.db")
cursor = connect.cursor()
cursor.execute(
    f"""CREATE TABLE IF NOT EXISTS companies (
        id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Date TEXT NOT NULL,
        Open REAL NOT NULL,
        High REAL NOT NULL,
        Low REAL NOT NULL,
        Close REAL NOT NULL,
        Adj_Close REAL NOT NULL,
        Volume INTEGER NOT NULL
)"""
)

# populate database with finance data
def add_to_db(name, fields):
    cursor.execute(
        f"""SELECT * FROM companies WHERE Date = '{fields[0]}' AND Name = '{name}'"""
    )
    if cursor.fetchone() is None:
        cursor.execute(
            f"""INSERT INTO companies (Name, Date, Open, High, Low, Close, Adj_CLose, Volume)
                        VALUES ('{name}', ?, ?, ?, ?, ?, ?, ?)""",
            fields,
        )
        connect.commit()


# requests to downloading the data from web-page
for company in companies:
    # responses from server
    response = requests.get(
        companies[company],
        headers=HEADERS,
    )

    for row in response.text.split("\n")[1:]:
        row = row.split(",")
        add_to_db(company, row)

connect.close()
