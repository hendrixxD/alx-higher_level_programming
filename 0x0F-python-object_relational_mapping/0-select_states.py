#!/usr/bin/python3
"""
list all states from ordered by id from
hbtn_0e_0_usa
"""
import MySQLdb as sql
from sys import argv


def main():
    """
    argument passed when initializing
    """

    USER = argv[1]
    PSWD = argv[2]
    DB = argv[3]

    d_b = sql.connect(host='localhost', user=USER,
            passwd=PSWD, db=DB, port = 3306)

    cur = d_b.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    # close cursor
    cur.close()
    # close connection
    d_b.close()


if __name__ == '__main__':
    main()
