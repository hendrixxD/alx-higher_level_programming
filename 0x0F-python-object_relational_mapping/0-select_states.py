#!/usr/bin/python3
import MySQLdb as sql
from sys import argv
def main():

    USER = argv[1]
    PSSWD = argv[2]
    DB = argv[3]

    d_b =sql.connect(host='localhost', user=USER, passwd=PSSWD, db='DB', port=3306)

    #cratong cursor
    cur = d_b.cursor()

    cur.execute("SELECT * FROM states ORDER BY(id)")

    rows = cur.fetchall()
    for row in rows:
        print(row)
