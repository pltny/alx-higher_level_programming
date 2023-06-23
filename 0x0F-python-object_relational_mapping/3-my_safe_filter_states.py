#!/usr/bin/python3

"""module - ensure """
import MySQLdb
from sys import argv

""" The function"""

if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name  BINARY"
            "'{:s}' ORDER BY id ASC".format(argv[4].replace("'", "''")))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
