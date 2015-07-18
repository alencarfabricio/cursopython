import sqlite3
db = sqlite3.connect("senac.db")
cursor = db.cursor()
cursor.execute("""CREATE TABLE verbo_conjugar (id integer primary key autoincrement,verbo varchar(40) not null,qt_vezes numeric(3) not null )""")
cursor.execute("""CREATE TABLE usuario (id integer primary key autoincrement,nome varchar(40) not null )""")
sql = "INSERT INTO verbo_conjugar (verbo, qt_vezes) VALUES ('LER', 1)"
cursor.execute(sql)
db.close() 
