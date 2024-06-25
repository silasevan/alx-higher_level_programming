#!/usr/bin/python3
from sqlalchemy import create_engine, exc
from sqlalchemy.engine import reflection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# Connection parameters
username = 'silasevan'
password = 'blessing'
host = 'localhost'
port = '3306'
database = 'hbtn_0e_0_usa'

# Create the connection string for connecting to the MySQL server (without a specific database)
server_connection_string = f'mysql+mysqldb://{username}:{password}@{host}:{port}/'

# Create the connection string for connecting to the specific database
database_connection_string = f'mysql+mysqldb://{username}:{password}@{host}:{port}/{database}'

# Connect to the MySQL server
try:
    server_engine = create_engine(server_connection_string)
    server_connection = server_engine.connect()
    print("Connected to the MySQL server")

    # Check if the database exists
    inspector = reflection.Inspector.from_engine(server_engine)
    databases = inspector.get_schema_names()
    if database not in databases:
        # Create the database if it does not exist
        server_connection.execute(f"CREATE DATABASE {database}")
        print(f"Database '{database}' created")

    server_connection.close()

    # Now connect to the specific database
    engine = create_engine(database_connection_string, echo=True)
    connection = engine.connect()
    print(f"Connected to the database '{database}'")
    # Define the table structure using the SQLAlchemy ORM
    Base = declarative_base()
    class State(Base):
        __tablename__ = 'states'

        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(256), nullable=False)
        

        def __repr__(self):
            return "<State(name='%s'>" % (
                                self.name, )
    
    
     # Create the table in the database
    Base.metadata.create_all(engine)
    print(f"Table '{State.__tablename__}' created")
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Insert multiple values into the table
    states = [
        State(name='California'),
        State(name='Texas'),
        State(name='New York'),
        State(name='Florida'),
        State(name='Illinois')
    ]
    session.add_all(states)

    # Commit the transaction
    session.commit()
    print("Inserted multiple values into the table")
    
    # Query and list all values from the table
    all_states = session.query(State).all()
    for state in all_states:
        print(f"({state.id}, '{state.name}')")
    
    
     # Close the session
    session.close()
    
    
    
    connection.close()
    
    

except exc.SQLAlchemyError as e:
    print(f"Error: {e}")
