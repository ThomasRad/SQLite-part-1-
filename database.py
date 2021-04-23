# Import package 
import sqlite3

# Connect to the database 
conn = sqlite3.connect('customer.db')

# Create a cursor 
c = conn.cursor()

# Create a Table
c.execute(""" CREATE TABLE customers (
	first_name text, 
	last_name text, 
	email text
	)""")

# Commit the command 
conn.commit()

# Now we close the connection. 
conn.close()

