#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
        cur = db.cursor()

        # Execute SQL query
        cur.execute("""SELECT * FROM states WHERE name
                    LIKE BINARY 'N%' ORDER BY states.id""")
        
        # Fetch and print results
        rows = cur.fetchall()
        for row in rows:
            print(row)
        
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
    
    finally:
        # Close cursor and database connection
        if 'cur' in locals() and cur is not None:
            cur.close()
        if 'db' in locals() and db is not None:
            db.close()
