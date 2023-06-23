#!/usr/bin/python3
""" <mysql username>
     <mysql password>
    <database name>
     <name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states
                WHERE name LIKE 
                ORDER BY """.format(sys.argv[4]).strip("'"))
    [print(state) for state in c.fetchall()]i
