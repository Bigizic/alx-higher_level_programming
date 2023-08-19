#!/usr/bin/python3

"""A script that prints all City objects from a database
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def model_city_fetch_by_state():
    """A function that takes 3 arguments from stdin, connects to a MySQL
    server running on localhost at port 3306 and prints all City objects
    from the database in ascending order by cities.id
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    # engine = create_engine(db_connect)
    Session = sessionmaker(bind=engine)
    session = Session()

    fetch_states = session.query(City, State).join(City.State)

    for city, state in fetch_states.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # session.commit()
    session.close()


if __name__ == '__main__':
    model_city_fetch_by_state()
