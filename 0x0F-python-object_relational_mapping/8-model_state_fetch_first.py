#!/usr/bin/python3

"""A script that prints the first State object from the database
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def model_state_fetch_first():
    """ A function that takes 3 arguments from stdin connect to my MySQL server
    running on localhost at port 3306 and prints the first State object from
    the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    fetch_first_state = session.query(State).order_by(State.id).first()
    if (fetch_first_state):
        print(fetch_first_state.id, fetch_first_state.name, sep=": ")
    else:
        print("Nothing")

    session.close()


if __name__ == '__main__':
    model_state_fetch_first()
