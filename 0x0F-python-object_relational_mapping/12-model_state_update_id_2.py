#!/usr/bin/python3

"""A script that changes the name of a State object from a database
"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def model_state_update_id_2():
    """A function that takes 3 arguments from stdin, connects to a MySQL server
    running on localhost at port 3306 and changes the name of the State table
    where id = 2 to New Mexico
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    id_search = session.query(State).get(2)

    if (id_search):
        id_search.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == '__main__':
    model_state_update_id_2()
