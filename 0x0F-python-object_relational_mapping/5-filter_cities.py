#!/usr/bin/python3
"""a sript that takes name of state as an argument
   and list all cities of that state"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    takes in 4 args:
    username, passwd, db_name, state_name
    """
    state_name = argv[4]
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()

    cur.execute("SELECT cities.name FROM states JOIN cities\
            ON states.id = cities.state_id\
            AND states.name = %s ORDER BY cities.id", (state_name, ))

    result = cur.fetchall()

    cities = []
    for row in result:
        cities.append(row[0])
    print(', '.join(cities))

    cur.close()
    db.close()
