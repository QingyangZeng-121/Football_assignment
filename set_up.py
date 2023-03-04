import decimal
import csv
import sqlite3
from datetime import datetime


conn = sqlite3.connect('events_football.db')
cur = conn.cursor()



conn.execute('DROP TABLE IF EXISTS event')
conn.execute('DROP TABLE IF EXISTS ginf')



conn.execute('CREATE TABLE event( id_event INTEGER PRIMARY KEY AUTOINCREMENT, sort_order TEXT, time TEXT, text TEXT, event_type TEXT, side TEXT, event_team TEXT, opponent TEXT, player TEXT, fastBreak TEXT)')
conn.execute('CREATE TABLE ginf( id_odsp INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, league TEXT, season TEXT, country TEXT, ht TEXT, at TEXT, fthg TEXT, ftag TEXT, odd_h TEXT, odd_d TEXT, odd_a TEXT)')



with open('archive/event.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for row in reader:
        print(row)

        id_event = row[0]
        sort_order = row[1]
        time = row[2]
        text = row[3]
        event_type = row[4]
        side = row[5]
        event_team = row[6]
        opponent = row[7]
        player = row[8]
        fastBreak = row[9]

        cur.execute('INSERT INTO event VALUES (?,?,?,?,?,?,?,?,?,?)', (id_event, sort_order, time, text, event_type, side, event_team, opponent, player, fastBreak))
        conn.commit()


with open('archive/ginf.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for row in reader:
        print(row)

        id_odsp = row[0]
        date = row[1]
        league = row[2]
        season = row[3]
        country = row[4]
        ht = row[5]
        at = row[6]
        fthg = row[7]
        ftag = row[8]
        odd_h = row[9]
        odd_d = row[10]
        odd_a = row[11]

        cur.execute('INSERT INTO ginf VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', (id_odsp, date, league, season, country, ht, at, fthg, ftag, odd_h, odd_d, odd_a))
        conn.commit()


print("data parsed successfully");

conn.close()


