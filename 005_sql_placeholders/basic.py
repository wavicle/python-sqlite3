import sqlite3

# First create the table and insert some data
connection = sqlite3.connect('mylocaldatabase.db')
cursor = connection.cursor()

cursor.execute('''
 CREATE TABLE person (
   first_name text,
   last_name text
 )
''')

insertSql = ''' 
INSERT INTO person (
  first_name,
  last_name
) VALUES (
  :firstName,
  :lastName
)
'''

cursor.execute(insertSql, {'firstName': 'Shashank', 'lastName': 'Araokar'})
cursor.execute(insertSql, {'firstName': 'Rutika', 'lastName': 'Ranjolkar'})

connection.commit()
connection.close()


# Show the entire world that you have two rows
connection = sqlite3.connect('mylocaldatabase.db')
connection.row_factory = sqlite3.Row

cursor = connection.cursor()
rows = cursor.execute('SELECT * FROM person')

print('Showing data before delete')
for row in rows:
  print ('Found name: ' + row['first_name'])


# Now delete one row and commit it
connection = sqlite3.connect('mylocaldatabase.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()
cursor.execute("DELETE FROM person WHERE first_name = :firstName", {'firstName': 'Shashank'})
connection.commit()

print('Showing data after delete')
cursor = connection.cursor()
rows = cursor.execute('SELECT * FROM person')
for row in rows:
  print ('Found name: ' + row['first_name'])

