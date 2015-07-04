import MySQLdb
con = MySQLdb.connect(host='localhost', user='root', passwd='',db='senac')

x = con.cursor()

x.execute("INSERT INTO alunos (nome_aluno, curso, turma, turno) VALUES ('Sergio','Python','TI','TARDE');")

con.commit()
