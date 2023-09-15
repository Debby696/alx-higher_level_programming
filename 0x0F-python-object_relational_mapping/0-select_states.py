#!/usr/bin/python3

"""
a script that lists all states from the database hbtn_0e_0_usa
"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    """ this connect to database """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    """ create a cursor object """
    cursor = db.cursor()

    """ write and execute the sql query """
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    """ fetch the results of the query """
    rows_selected = cursor.fetchall()

    """ print the results """
    for row in rows_selected:
        print(row)
