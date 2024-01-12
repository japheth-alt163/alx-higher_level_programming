#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def list_states(username, password, db_name):
    """
    Lists all states from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to retrieve states
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)

        # Fetch all the rows and display the results
        for row in cursor.fetchall():
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    """
    Main function to run the script.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
