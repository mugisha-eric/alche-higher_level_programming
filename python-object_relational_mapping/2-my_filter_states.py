#!/usr/bin/python3
"""Displays all values in the states table whose name matches a given argument.

Database: hbtn_0e_0_usa. Uses string formatting to build the SQL query
(not safe from SQL injection; see 3-my_safe_filter_states.py for safe version).

Usage: ./2-my_filter_states.py <mysql username> <mysql password>
                               <database name> <state name searched>
Results are ordered by ascending states.id.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
