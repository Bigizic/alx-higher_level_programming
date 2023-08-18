#!/usr/bin/python3

"""A script that lists all states objects from a database
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def model_state_fetch_all():
    """A script that takes 3 arguments from stdin connect to a MySQL server
    running on localhost at port 3306
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    fetch_states = session.query(State).order_by(State.id)

    for state in fetch_states:
        print(state.id, state.name, sep=": ")

    session.close()


if __name__ == '__main__':
    model_state_fetch_all()
