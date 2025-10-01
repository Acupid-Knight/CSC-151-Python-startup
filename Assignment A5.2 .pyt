##############################

# Clear the terminal screen
import sqlite3
import os
os.system('clear')

##############################
# SQLite Database
##############################

conn = sqlite3.connect('customer.db')
# Create a cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE customer (
            first_name text,
            last_name texxt,
            email text
            )""")
'''

# c.execute("INSERT INTO customer VALUES ('Antonio', 'Mack', 'antoniomack2007@gmail.com')")

c.execute("SELECT * FROM customer")
items = c.fetchall()

for item in items:
    print(item[0] + "" + item[1])

# Commit our changes
conn.commit()


# Close database connection
conn.close()