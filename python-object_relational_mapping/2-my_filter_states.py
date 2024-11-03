#!/usr/bin/python3
"""Module for Selecting states where name equals argument"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (argv[4],))
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
