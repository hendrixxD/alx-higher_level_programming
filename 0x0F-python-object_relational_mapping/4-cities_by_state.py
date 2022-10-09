#!/usr/bin/python3
"""query and list all states but usage of execute is once"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    takes in three args:
    username, passwd, db_name
    """

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
