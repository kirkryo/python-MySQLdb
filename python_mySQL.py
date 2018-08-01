import MySQLdb

# database details
host = 'localhost'
user = 'root'
password = ''
name = 'data_manager'

db = MySQLdb.connect(host, user, password, name)

# create cursor object
c = db.cursor()

id = 37

# execute SQL query.
# adding the comma inside the (id,) will convert it to a tuple
# otherwise it will be of type int or str - and those are not iterable
# tuples are immutable
c.execute("SELECT * FROM photos WHERE id = %s", (id,))

# display the results from the query
for row in c.fetchall():
    print(row)
