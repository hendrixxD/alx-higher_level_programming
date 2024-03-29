#!/usr/bin/python3
"""list search states"""
import MySQLdb
import sys

if __name__ == "__main__":

    state_name = sys.argv[4]
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    # Start cursor
    cur = conn.cursor()

    # Query
    cur.execute("SELECT * FROM states WHERE name = '{}' \
            ORDER BY id ASC".format(state_name))
    rows = cur.fetchall()

    # Print query
    for row in rows:
        if row[1] == state_name:
            print(row)

    # Close cursor
    cur.close()
    conn.close()
