#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv
    uinput = argv[4]
    """ this connect to database """
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    """ create a cursor object """
    cursor = db.cursor()

    """ write and execute the sql query """
    query = "SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id \
    WHERE states.name = %s ORDER BY cities.id ASC;"

    cursor.execute(query, (uinput,))

    """ fetch the results of the query """
    rows_selected = cursor.fetchall()

    """ print the results """
    if rows_selected is not None:
        print(", ".join([row[0] for row in rows_selected]))
