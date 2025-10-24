import sqlite3
con = sqlite3.connect('SocialNet6.db')
cur = con.cursor()

cur.execute("CREATE TEMP TABLE SocialNet(Name text, Likes text)")
cur.execute("INSERT INTO SocialNet VALUES('Denny', 'Beata')")
cur.execute("INSERT INTO SocialNet VALUES('Denny', 'John')")
cur.execute("INSERT INTO SocialNet VALUES('Beata', 'Denny')")
cur.execute("INSERT INTO SocialNet VALUES('Beata', 'Mary')")
cur.execute("INSERT INTO SocialNet VALUES('Mary', 'John')")
cur.execute("INSERT INTO SocialNet VALUES('John', 'Beata')")
cur.execute("INSERT INTO SocialNet VALUES('John', 'Mary')")
cur.execute("INSERT INTO SocialNet VALUES('John', 'Denny')")

cur.execute("CREATE TEMP TABLE Travel (Name text, City text, Days integer)")
cur.execute("INSERT INTO Travel VALUES('Denny', 'Beijing', 3)")
cur.execute("INSERT INTO Travel VALUES('Denny', 'Paris', 5)")
cur.execute("INSERT INTO Travel VALUES('Beata', 'Paris', 5)")
cur.execute("INSERT INTO Travel VALUES('Beata', 'Chicago', 5)")
cur.execute("INSERT INTO Travel VALUES('Beata', 'Bogota', 3)")
cur.execute("INSERT INTO Travel VALUES('Beata', 'Beijing', 2)")
cur.execute("INSERT INTO Travel VALUES('Mary', 'Chicago', 3)")
cur.execute("INSERT INTO Travel VALUES('Mary', 'Paris', 2)")
cur.execute("INSERT INTO Travel VALUES('Mary', 'Nairobi', 5)")
cur.execute("INSERT INTO Travel VALUES('John', 'Nairobi', 7)")
cur.execute("INSERT INTO Travel VALUES('John', 'Bogota', 2)")
con.commit()

print ('Query 1')
print ('1. List all data in SocialNet')
print ("Query 1 Results")
cur.execute('SELECT * FROM SocialNet')
for record in cur:
    print(record)
print ('')

print ('Query 2')
print ('2. List all people who are liked in SocialNet with no repetitions')
print ("Query 2 Results")
cur.execute('SELECT DISTINCT Likes FROM SocialNet')
for record in cur:
    print(record)
print ('')

print ('Query 3')
print ('3. List all cities that were visited by people from our database with no repetitions.')
print ("Query 3 Results")
cur.execute('SELECT DISTINCT City FROM Travel')
for record in cur:
    print(record)
print ('')

print ('Query 4')
print ('4. Who traveled to Paris?')
print ("Query 4 Results")
cur.execute('SELECT Name FROM Travel WHERE City = "Paris"')
for record in cur:
    print(record)
print ('')

print ('Query 5')
print ('5. List all people in SocialNet who like John')
print ("Query 5 Results")
cur.execute('SELECT Name FROM SocialNet WHERE Likes = "John"')
for record in cur:
    print(record)
print ('')

print ('Query 6')
print ('6. List all people who traveled exactly for five days')
print ("Query 6 Results")
cur.execute('SELECT DISTINCT Name FROM Travel WHERE Days = 5')
for record in cur:
    print(record)
print ('')

print ('Query 7')
print ('7. How many times each person was travelling')
print ("Query 7 Results")
cur.execute('SELECT Name, COUNT(City) FROM Travel GROUP BY Name')
for record in cur:
    print(record)
print ('')

print ('Query 8')
print ('8. How many people each person likes?')
print ("Query 8 Results")
cur.execute('SELECT Name, COUNT(Likes) FROM SocialNet GROUP BY Name')
for record in cur:
    print(record)
print ('')

print ('Query 9')
print ('9. How many times each city each person visited?')
print ("Query 9 Results")
cur.execute('SELECT Name, City, COUNT(*) FROM Travel GROUP BY Name, City')
for record in cur:
    print(record)
print ('')

print ('Query 10')
print ('10. List the name of each person who likes people who visited Bogota')
print ("Query 10 Results")
cur.execute('SELECT DISTINCT S.Name \
             FROM SocialNet S, Travel T \
             WHERE S.Likes = T.Name AND T.City = "Bogota"')
for record in cur:
    print(record)
print ('')

print ('Query 11')
print ('11. List places that were visited by people that Denny likes.')
print ("Query 11 Results")
cur.execute('SELECT DISTINCT T.City \
             FROM Travel T, SocialNet S \
             WHERE S.Name = "Denny" AND S.Likes = T.Name')
for record in cur:
    print(record)
print ('')

print ('Query 12')
print ('12. Compute total days of traveling by people that Denny likes.')
print ("Query 12 Results")
cur.execute('SELECT SUM(T.Days) \
             FROM Travel T, SocialNet S \
             WHERE S.Name = "Denny" AND S.Likes = T.Name')
for record in cur:
    print(record)
print ('')

con.close()
