#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in c.fetchall()]
