import MySQLdb


def refresh(model):
	con = MySQLdb.connect("localhost", "root", "tom")
        con.select_db("ficher")
        cursor = con.cursor()
	cursor.execute("select nome, mat from minicurso")
	model.clear()
        b = cursor.fetchall()
 	for linha in b:
            model.append([linha[0], linha[1]])
     
def refresh2():
	cadastrados = []
	con = MySQLdb.connect("localhost", "root", "tom")
	con.select_db("ficher")
	cursor = con.cursor()
	cursor.execute("select * from minicurso")
	b = cursor.fetchall()
	for linhas in b:
		cadastrados.append({'nome':linhas[1], 'matricula':linhas[2], 'curso':linhas[3], 'email':linhas[4]})
	return(cadastrados)

def refresh3():
	con = MySQLdb.connect("localhost", "root", "tom")
	con.select_db("ficher")
	cursor = con.cursor()
	cursor.execute("select * from minicurso")
	b = cursor.fetchall()
	return(b)

def enviar_site(server, usuario, senha, tupla, linhas):
	con = MySQLdb.connect(server, usuario, senha)
	cursor = con.cursor()
	try:
		con.select_db("ficher")
	except:
		cursor.execute("create database ficher")
		con.select_db("ficher")
	try:
		cursor.execute("select * from ficher")
	except:
		cursor.execute("create table ficher(nome char(60), mat char(60), curso char(60), email char(60))")
	for i in linhas:
		cursor.execute('insert into ficher (%s, %s, %s, %s)', (i[1]['nome'], i[2]['matricula'], i[3]['curso'], i[4]['email']))
