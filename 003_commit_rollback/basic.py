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
connection.commit()

cursor.execute('''
  INSERT INTO person (
    first_name,
    last_name
  ) VALUES (
    'Rutika',
    'Ranjolkar'
  )
''')
connection.rollback()

connection.close()

connection = sqlite3.connect('mylocaldatabase.db')
connection.row_factory = sqlite3.Row

cursor = connection.cursor()
rows = cursor.execute('SELECT * FROM person')

for row in rows:
  print ('Found name: ' + row['first_name'])

