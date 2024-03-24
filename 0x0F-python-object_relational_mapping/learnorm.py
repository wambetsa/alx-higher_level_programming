select * from users where zipcode=94107
user = Users.object.filter(zipcode=94107)

import MySQLdb from _mysql
db = _mysql.connect(host="localhost", user="joebob",
                    password="moonpie", database="thangs")
db = _mysql.connect(host, port, password, database)
db=_mysql.connect(host, database, read_default_file)

db.query("""SELECT name, age, details from users WHERE price = '%ohn'""")

r=db.store_result()#fetches result once. RECOMMENDED set LIMIT eg LIMIT=1000
r=db.use_result()#ties up database and connection

r.fetch_row()
r.fetch_row(maxrows=0, how=1)



import MySQLdb
db = MySQLdb.connect(password, database)
db.cursor()
max_size = 5
c.execute("""SELECT name, id, age FROM users WHERE age < %s""", (max_size,))




db = MySQLdb.connect(host="localhost", user="root", password="r123", database="jt")
db.query("""SELECT""")
db.store_result()
db.fetch_row()


db = MySQLdb.connect(host="localhost", user="root", password="r123", database="jt")
cur = db.cursor()
cur.execute("CREATE TABLE song (id INT PRIMARY KEY AUTO_INCREMENT, name TEXT NOT NULL, age INT)")

#Execute insert SINGLE SUBSTITUTION QUERY
songs = ("rhumba", "gospel", "reggae", "hip hop")
for song in songs:
    cur.execute("INSERT INTO song (title) VALUES (%s)", song)
    print("Auto increment ID: %s", %cur.lastrowid)

#MULTIPLE SUBSTITUTION QUERIES
cur.execute("SELECT * FROM song WHERE id = %s or id = %s", (1,2))

numrows = cur.execute("SELECT * FROM song")
print "Selected %s rows" % numrows
print "Selected %s rows" % cur.rowcount


# OBTAINING QUERY RESULTS
cur.execute("SELECT * FROM song")
rows = cur.fetchall()
for row in rows:
    for col in row:
        print "%s," % col
    print "\n"


# FETCH ONE BY ONE
cur.execute("SELECT * FROM song")
print "ID: %s -- Title: %s" % cur.fetchone()


# EXCEPTION AND ERRORS
try:
    cur.execute("SELECT * FROM song")
    rows = cur.fetchall()
except MySQLdb, error, e:
    try:
        print "MySQL Error [0]: %s" % (e.agrs[0], e.args[1])
    except IndexError:
        print "MySQL Error is: %s" % str(e)
for row in rows:
    for col in row:
        print "%s," % col
    print "\n"


# CLEAN UP
cur.close()# close all cursors
db.close()# close all database connections
