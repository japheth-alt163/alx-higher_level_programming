#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create a connection to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database), pool_pre_ping=True)

    # Create all the tables in the database
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = Session(bind=engine)

    # Create a new State object
    new_state = State(name="California")

    # Create a new City object
    new_city = City(name="San Francisco")

    # Add the new City to the new State
    new_state.cities.append(new_city)

    # Add the new State to the session
    Session.add(new_state)

    # Commit the changes to the database
    Session.commit()

    # Close the session
    Session.close()
