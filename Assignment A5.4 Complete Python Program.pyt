import sqlite3

# ------------------------------------------------------------
# Quiz 2 Practice SQL — CSC205 Spring 2020
# Antonio Mack
# ------------------------------------------------------------

# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# ------------------------------------------------------------
# Step 1: Create Tables
# ------------------------------------------------------------
cursor.execute('''
CREATE TABLE COMPANY (
    CName TEXT PRIMARY KEY,
    StockPrice REAL,
    Country TEXT
);
''')

cursor.execute('''
CREATE TABLE PRODUCT (
    PName TEXT,
    Price REAL,
    Category TEXT,
    Manufacturer TEXT,
    FOREIGN KEY (Manufacturer) REFERENCES COMPANY(CName)
);
''')

# ------------------------------------------------------------
# Step 2: Insert Data
# ------------------------------------------------------------
companies = [
    ('GizmoWorks', 25, 'USA'),
    ('Canon', 65, 'Japan'),
    ('Hitachi', 15, 'Japan')
]
products = [
    ('Gizmo', 19.99, 'Gadgets', 'GizmoWorks'),
    ('Powergizmo', 29.99, 'Gadgets', 'GizmoWorks'),
    ('SingleTouch', 149.99, 'Photography', 'Canon'),
    ('MultiTouch', 203.99, 'Household', 'Hitachi')
]

cursor.executemany('INSERT INTO COMPANY VALUES (?, ?, ?);', companies)
cursor.executemany('INSERT INTO PRODUCT VALUES (?, ?, ?, ?);', products)

# ------------------------------------------------------------
# Step 3: Execute Queries
# ------------------------------------------------------------
print("1. List all categories of products (with no duplicates).")
cursor.execute('SELECT DISTINCT Category AS ProductCategory FROM PRODUCT;')
print("ProductCategory")
for row in cursor.fetchall():
    print(row[0])
print()

print("2. List all categories of products produced by the company GizmoWorks (no duplicates).")
cursor.execute('''
SELECT DISTINCT Category AS ProductsGizmoWorks
FROM PRODUCT
WHERE Manufacturer = "GizmoWorks";
''')
print("ProductsGizmoWorks")
for row in cursor.fetchall():
    print(row[0])
print()

print("3. In what country is the company GizmoWorks located?")
cursor.execute('''
SELECT Country
FROM COMPANY
WHERE CName = "GizmoWorks";
''')
print("Country")
for row in cursor.fetchall():
    print(row[0])
print()

print("4. List all companies located in Japan in alphabetical order.")
cursor.execute('''
SELECT CName AS CompanyName
FROM COMPANY
WHERE Country = "Japan"
ORDER BY CName ASC;
''')
print("CompanyName")
for row in cursor.fetchall():
    print(row[0])
print()

print("5. How many companies are located in Japan?")
cursor.execute('''
SELECT COUNT(*) AS NumberOfCompanies
FROM COMPANY
WHERE Country = "Japan";
''')
print("NumberOfCompanies")
for row in cursor.fetchall():
    print(row[0])
print()

print("6. What is the price of 1000 products called Gizmo?")
cursor.execute('''
SELECT 1000 * Price AS Price1000Gizmo
FROM PRODUCT
WHERE PName = "Gizmo";
''')
print("Price1000Gizmo")
for row in cursor.fetchall():
    print(int(row[0]))  # Make it an integer (19990)
print()

print("7. What is the total price if a customer orders 1000 of each product?")
cursor.execute('''
SELECT SUM(1000 * Price) AS TotalPrice
FROM PRODUCT;
''')
total = cursor.fetchone()[0]
print("TotalPriceForAllProducts")
print(total)
print()

print("8. List all possible pairs of product name and the country it is produced.")
cursor.execute('''
SELECT P.PName AS ProductName, C.Country
FROM PRODUCT P
JOIN COMPANY C ON P.Manufacturer = C.CName;
''')
print("ProductName\tCountry")
for row in cursor.fetchall():
    print(f"{row[0]}\t{row[1]}")
print()

print("9. Find all Japanese company names that manufacture household products.")
cursor.execute('''
SELECT DISTINCT C.CName AS JapaneseCompanies
FROM COMPANY C
JOIN PRODUCT P ON C.CName = P.Manufacturer
WHERE C.Country = "Japan" AND P.Category = "Household";
''')
print("JapaneseCompanies")
for row in cursor.fetchall():
    print(row[0])
print()

print("10. List all product prices that were manufactured by USA companies.")
cursor.execute('''
SELECT '$' || Price AS USProductPrice
FROM PRODUCT P
JOIN COMPANY C ON P.Manufacturer = C.CName
WHERE C.Country = "USA";
''')
print("USProductPrice")
for row in cursor.fetchall():
    print(row[0])
print()

print("11. List total of all product prices that were manufactured by each country.")
cursor.execute('''
SELECT C.Country, SUM(P.Price) AS TotalPrice
FROM PRODUCT P
JOIN COMPANY C ON P.Manufacturer = C.CName
GROUP BY C.Country;
''')
print("Country\tTotalPrice")
for row in cursor.fetchall():
    print(f"{row[0]}\t{row[1]}")
print()

# ------------------------------------------------------------
# Cleanup
# ------------------------------------------------------------
conn.close()
