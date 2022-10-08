#!/usr/bin/python3
#Introduction to MYSQL in python

import MySQLdb as sql
#from PyMySQL import * as MySQLdb

#connecting to MyAQL database
db = sql.connect(host='localhost', user='root', passwd='password', db='MySQL_python')

#Creating a cursor
cur = db.cursor()

#Executing MySQL Queries in python
cur.execute("CREATE TABLE song (id INT UNSIGNED PRIMARY KEY AUTO_INCREAMENT, title TEXT NOT NULL);")

#Execute Insert / Single Substitution Query
songs = ('Purple haze', 'All Along the watch Tower', 'Foxy Lady')
for song in songs:
    cur.execute("INSERT INTO song (title) VALUES (%s)", song)
    #cur.execute(f'INSERT INTO song (title) VALUES {song}')

    #print "Auto Increment ID: %s" % cur.lastrowid
    print(f"Auto Increament ID: {cur.lastrowid}")

#Multiple Substitution Query
cur.execute('SELECT * FROM song WHERE id = %s or id = %s', (1, 2))

#Execute SELECT
numrows = cur.execute('SELECT * FROM song')
print(f'Selected {numrows}')
print(f'Selected {cur.rowcount}')

#OBTAINING QUERY RESULTS
#fetch All-at-Once
cur.execute('SELECT * FROM somg')
rows = cur.fetchall()
for row in rows:
    for col in row:
        print(f'{col}')
    print("\n")

#Fetch One-At-A-Time
cur.execute("SELECT * FROM song WHERE id = 1")
print(f"ID: {cur.fetchone()}  --  Title: {cur.fetchone()}")

#close all cursors
cur.close()

#Close all databases
db.close()
