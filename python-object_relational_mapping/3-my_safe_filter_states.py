#!/usr/bin/python3
"""Displays states matching a given argument. Safe from SQL injection.

Fetches all rows first then filters in Python, avoiding user input ever
touching the SQL string.

Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password>
                                    <database name> <state name searched>
Results are ordered by ascending states.id.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
