#!/usr/bin/python3

"""A script that lists all State objects, and corresponding City
objects, contained in the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    u_name, ps_wd, d_b = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(u_name, ps_wd, d_b), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    fetch_data = session.query(State).order_by(State.id).all()

    for state in fetch_data:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
