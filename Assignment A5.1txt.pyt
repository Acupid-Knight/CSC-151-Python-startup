

# Create a cursor
cur = conn.cursor()

# Test data
names_list = [
    ("Roderick", "Watson"),
    ("Roger", "Hom"),
    ("Petri", "Halonen"),
    ("Jussi", ""),
    ("James", "McCann"),
]

# Insert data into database
curr.executemany('''
                 INSERT INTO people (first_name, last_name) VALUES (?, ?)
              ''', names_list)
conn.commit()  
              
# Close db objects
cur.close()
conn.close()