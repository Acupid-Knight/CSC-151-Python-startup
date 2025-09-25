import sqlite3

# Conncet to a (new) database
conn = sqlite3.connect("D:\\demo\\alpha.db")

# Create a cursor
cur = conn.cursor()

# Create a "people" table
conn.execute('''CREATE TABLE IF NOT EXISTS people
               (first _name TEXT, last_name TEXT)''')

# Close db objects
cur.close()
conn.close()