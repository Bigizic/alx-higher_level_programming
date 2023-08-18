#!/usr/bin/python3

"""A script that lists all State objects that contain the letter a from a
database
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def model_state_filter_a():
    """A function that takes 3 arguments from stdin and connect to a MySQL
    server running on localhost on port 3306, proceeds to list all State
    objects that contain the letter a from the database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    fetch_states = session.query(State).filter(
                   State.name.like('%a%')).order_by(State.id)
    for states in fetch_states:
        print(states.id, states.name, sep=": ")

    session.close()


if __name__ == '__main__':
    model_state_filter_a()
