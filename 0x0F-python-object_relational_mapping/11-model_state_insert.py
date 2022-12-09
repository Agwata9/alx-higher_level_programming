#!/usr/bin/python3
# Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
# Usage: ./11-model_state_insert.py <mysql username> /
#                                   <mysql password> /
#                                   <database name>
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base,State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    # create a session
    session = Session()

    # create the object and add it
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # print state.id
    state_add = session.query(State).filter(State.name == 'Louisiana').one()
    print(state_add.id)

    session.close()


