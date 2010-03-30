#isso é tabelaO

from pyExcelerator import *
import funcoes
import os

cadastrados = funcoes.refresh2()

def criar_tabela():
	wb = Workbook()
	ws0 = wb.add_sheet('cadastrados')
	cabecario = ('Nome', 'Matricula', 'Email', 'Curso')
	
	for d in range(len(cabecario)):
		ws0.write(0,d,cabecario[d])

	rows=[]
	for i in cadastrados:
		rows.append((i['nome'],i['matricula'],i['email'],i['curso']))
	
	rowcont = 1

	for row in rows:
		for x in range(len(row)):
			ws0.write(rowcont,x, row[x])
		rowcont +=1

	wb.save('lista.xls')
	os.system("openoffice.org lista.xls")


