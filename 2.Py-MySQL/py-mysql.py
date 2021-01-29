import mysql.connector

dbapi = mysql.connector.connect(
	host='127.0.0.1',
	user='userdb',
	passwd='123abc',
	database='MYBLOG'
	)

mycursor = dbapi.cursor()

#def show_tabs(curs):
#	sql = 'SHOW TABLES'
#	curs.execute(sql)
#	for x in curs:
#		print(x)

#show_tabs(mycursor)
#print()
#
#
#def desc_tabs(curs,tab:str):
#	curs.execute('DESCRIBE {}'.format(tab))
#	for x in curs:
#		print(x)
#
#desc_tabs(mycursor, 'INSCRITOS')
#print()

def inscritos_tema(curs,tema_id:int):
	sql = 'SELECT INSC.NOME AS Nome, INSC.EMAIL AS Email\
           FROM INSCRITOS INSC LEFT JOIN RELACIONA RE ON RE.ID_INSCRITO = INSC.IDINSCRITO\
           LEFT JOIN TEMAS TM ON RE.ID_TEMA = TM.IDTEMA WHERE TM.IDTEMA = {}\
           AND INSC.IDINSCRITO != 1\
           GROUP BY INSC.NOME, INSC.EMAIL\
           ORDER BY INSC.NOME'.format(tema_id)
	curs.execute(sql)
	myresult = curs.fetchall()
	json_t = []
	for i in range(len(myresult)):
		json_t.append({})
		json_t[i]['nome'] = myresult[i][0]
		json_t[i]['email'] = myresult[i][1]
	
	return json_t

aux = inscritos_tema(mycursor,4)
print(aux)
print()



def temas_ids(curs,var:int):
	sql = 'SELECT TM.IDTEMA AS id, TM.TEMA AS TEMA FROM TEMAS TM\
	       WHERE TM.IDTEMA = {p}'.format(p=var)
	curs.execute(sql)
	myresult = curs.fetchall()
	json_t = []
	for i in range(len(myresult)):
		json_t.append({})
		json_t[i]['id'] = myresult[i][0]
		json_t[i]['tema'] = myresult[i][1]
	
	return json_t

aux2 = temas_ids(mycursor, '3')
print(aux2)
print()


sql = 'INSERT INTO INSCRITOS (NOME, EMAIL, TELEFONE) VALUES (%s, %s, %s)'
val = ('John Locke', 'highway2@locke.com', '19 88945 6110')
mycursor.execute(sql, val)
dbapi.commit()


mycursor.close()

dbapi.close()

exit()