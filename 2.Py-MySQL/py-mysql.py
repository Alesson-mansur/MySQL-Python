import mysql.connector

# Conectando e autenticando no banco
dbapi = mysql.connector.connect(
	host='127.0.0.1',
	user='userapi',
	passwd='123456',
	database='MYBLOG'
	)


# Variável que aponta, estabelece a conexão e executa comandos no banco
mycursor = dbapi.cursor()


# Mostrar as tabelas do banco
def show_tabs(curs):
	curs.execute('SHOW TABLES')
	for x in curs:
		print(x)

show_tabs(mycursor)
print()


# Descrição das características e elementos da tabela
#def desc_tabs(curs,tab:str):
#	curs.execute('DESCRIBE {}'.format(tab))
#	print(tab + ':')
#	for x in curs:
#		print(x)

#desc_tabs(mycursor,'INSCRITOS')
#print()
#
#desc_tabs(mycursor,'TEMAS')
#print()

# Fecha/encerra o ponteiro de conexão com o banco
mycursor.close()

# Fecha a conexão com o banco
dbapi.close()

# Encerra conexões com o banco
exit()


## Retorna o ID de um tópico dado um nome de tópico
#def tema_ids(curs,var:str):
#	sql = 'SELECT TM.IDTEMA AS ID, TM.TEMA AS Tópico FROM TEMAS TM\
#	       WHERE TM.TEMA LIKE "%{}%"'.format(var)
#	curs.execute(sql)
#	myresult = curs.fetchall() #busca todos os resultados da consulta e retorna um objeto list
#	json_f = []
#	for i in range(len(myresult)):
#		json_f.append({})
#		json_f[i]['id'] = str(myresult[i][0]) 
#		json_f[i]['tema'] = str(myresult[i][1])
#
#	return json_f
#
#results = tema_ids(mycursor, 'C')
#print(results)
#print()
#
#
## Retorna os nomes e os emails dos inscritos interessados em um tópico específico
#def inscritos_tema(curs,tema_id:int,qtd=100):
#	
#
#Lista = inscritos_tema(mycursor,3)
#print(Lista)
#print()
#
#
## Fecha/encerra o ponteiro de conexão com o banco
#mycursor.close()
#
## Fecha a conexão com o banco
#dbapi.close()
#
## Encerra conexões com o banco
#exit()
##-------------------------------------------------------