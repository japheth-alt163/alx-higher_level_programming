#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a MySQL cursor
    cursor = db.cursor()

    # Execute the parameterized query to retrieve cities of the specified state
    query = """SELECT GROUP_CONCAT(name ORDER BY id ASC SEPARATOR ', ')
               FROM cities
               WHERE state_id IN (SELECT id FROM states WHERE name = %s)"""
    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()

    # Display the results
    if result[0]:
        print(result[0])
    else:
        print()

    # Close the cursor and connection
    cursor.close()
    db.close()
