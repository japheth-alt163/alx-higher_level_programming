#!/usr/bin/python3
"""Script that lists all City objects from the database hbtn_0e_101_usa"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Set up the connection to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the database and print City objects with associated State
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
