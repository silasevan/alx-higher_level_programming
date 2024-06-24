#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    
    # Create a cursor object to interact with the database
    cursor = db.cursor()
    
    # Execute the query to select all states ordered by id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    
    # Fetch all the results
    results = cursor.fetchall()
    
    # Print each state
    for row in results:
        print(row)
    
    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)
