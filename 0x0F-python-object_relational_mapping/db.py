import MySQLdb

con = MySQLdb.connect(host="localhost",user="root",database="mysql")
cur = con.cursor()
cur.execute("SELECT * FROM columns_priv")
query_rows = cur.fetchall()
for r in query_rows:
    print(r)
cur.close()
con.close()



# WITH ORM
engine = create_engine('mysql+mysqldb://{}:{}@licalhost/{}'.format("root","root","my_db"), pool_pre_ping=True)
Base.metadata.create_engine(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()