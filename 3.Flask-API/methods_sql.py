import mysql.connector

def inscritos_tema(curs,tema_id:int):
	sql = 'SELECT INSC.NOME AS Nome, INSC.EMAIL AS Email\
           FROM INSCRITOS INSC LEFT JOIN RELACIONA RE ON RE.ID_INSCRITO = INSC.IDINSCRITO\
           LEFT JOIN TEMAS TM ON RE.ID_TEMA = TM.IDTEMA WHERE TM.IDTEMA = {r}\
           AND INSC.IDINSCRITO != 1\
           GROUP BY INSC.NOME, INSC.EMAIL\
           ORDER BY INSC.NOME'.format(r=tema_id)
	curs.execute(sql)
	myresult = curs.fetchall()
	json_t = []
	for i in range(len(myresult)):
		json_t.append({})
		json_t[i]['nome'] = myresult[i][0]
		json_t[i]['email'] = myresult[i][1]
	
	return json_t


def temas_ids(curs,var:int):
	sql = 'SELECT TM.IDTEMA AS id, TM.TEMA AS Tema FROM TEMAS TM\
	       WHERE TM.IDTEMA = {p}\
	       AND TM.IDTEMA != 1'.format(p=var)
	curs.execute(sql)
	myresult = curs.fetchall()
	json_t = []
	for i in range(len(myresult)):
		json_t.append({})
		json_t[i]['id'] = myresult[i][0]
		json_t[i]['tema'] = myresult[i][1]
	
	return json_t


def temas_all(curs):
	sql = 'SELECT TM.IDTEMA AS id, TM.TEMA AS Tema FROM TEMAS TM WHERE TM.IDTEMA != 1'
	curs.execute(sql)
	myresult = curs.fetchall()
	json_t = []
	for i in range(len(myresult)):
		json_t.append({})
		json_t[i]['id'] = myresult[i][0]
		json_t[i]['tema'] = myresult[i][1]
	
	return json_t


def credentials(curs,usernm:str):
	sql = 'SELECT USR.USERNAME AS User, USR.PASSWORD AS Pwd FROM USERS USR\
	       WHERE USR.USERNAME = "{r}"'.format(r=usernm)
	curs.execute(sql)
	myresult = curs.fetchall()
	value = {}
	value['User'] = myresult[0][0]
	value['Pwd'] = myresult[0][1]
	
	return value