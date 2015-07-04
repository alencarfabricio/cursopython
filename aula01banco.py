"""
Aula 02 - Conectando com banco de dados
senac e o nome do meu banco de dados
alunos e a minha tabela no banco de dados senac.
fetchall = busca todas as linhas q foi selecionada 
"""

import MySQLdb
con = MySQLdb.connect(host='localhost', user='root', passwd='',db='senac')

x = con.cursor()

# Incluindo dados no banco senac na tabela aluno
#x.execute("INSERT INTO alunos (nome_aluno, curso, turma, turno) VALUES ('Sergio','Python','TI','TARDE');")
#x.execute("INSERT INTO alunos (nome_aluno, curso, turma, turno) VALUES ('Sergio','Python','TI','TARDE');")
#x.execute("INSERT INTO alunos (nome_aluno, curso, turma, turno) VALUES ('Fabio','Python','TI','TARDE');")
#x.execute("INSERT INTO alunos (nome_aluno, curso, turma, turno) VALUES ('Lenno','Python','TI','TARDE');")
#x.execute("INSERT INTO alunos (nome_aluno, curso, turma, turno) VALUES ('Rogerio','Python','TI','TARDE');")
#x.execute("INSERT INTO alunos (nome_aluno, curso, turma, turno) VALUES ('Gilmar','Python','TI','TARDE');")
#x.execute("INSERT INTO alunos (nome_aluno, curso, turma, turno) VALUES ('Vicente','Python','TI','TARDE');")




# Consultar um registro no banco
#x.execute("SELECT * FROM alunos where nome_aluno = 'Sergio'");

# Deletar um registro no banco
#x.execute("DELETE FROM alunos WHERE nome_aluno = 'Sergio'");

# Alterar dados no banco
x.execute ("UPDATE alunos SET nome_aluno='Fabricio' WHERE nome_aluno = 'Vicente'");

print x.fetchall()      

con.commit()
con.close()
