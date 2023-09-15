#!/usr/bin/python3

"""
a script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':

    """ this connect to database """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    """ create a cursor object """
    cursor = db.cursor()

    """ write and execute the sql query """
    with db.cursor() as db_cursor:
        db_cursor.execute("SELECT cities.id, cities.name, states.name \
                            FROM cities JOIN states ON cities.state_id \
                            ORDER BY cities.id ASC")

    """ fetch the results of the query """
    rows_selected = db_cursor.fetchall()

    """ print the results """
    if rows_selected is not None:
        for row in rows_selected:
            print(row)

    cursor.close()
    db.close()
