import sqlite3

connection = sqlite3.connect('mylocaldatabase.db')
cursor = connection.cursor()

cursor.execute('''
 CREATE TABLE person (
   first_name text,
   last_name text
 )
''')

cursor.execute('''
  INSERT INTO person (
    first_name,
    last_name
  ) VALUES (
    'Shashank',
    'Araokar'
  )
''')

cursor.execute('''
  INSERT INTO person (
    first_name,
    last_name
  ) VALUES (
    'Rutika',
    'Ranjolkar'
  )
''')

connection.commit()
connection.close()

connection = sqlite3.connect('mylocaldatabase.db')
cursor = connection.cursor()
rows = cursor.execute('SELECT * FROM person')

for row in rows:
  print (row)

connection.close()
