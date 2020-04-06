import sqlite3

# connect the sqlitedb
conn = sqlite3.connect('project.db')
c = conn.cursor()

serviceTable = c.execute('select * from services')
for row in serviceTable:
    print(row)