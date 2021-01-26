sql = 'INSERT INTO INSCRITOS (NOME, EMAIL, TELEFONE) VALUES (%s, %s, %s)'
val = ('John Locke', 'highway2@locke.com', '19 88945 6110')
mycursor.execute(sql, val)
dbapi.commit()


def select_all(curs,table:str):
	sql = 'SELECT * FROM {}'.format(table)
	curs.execute(sql)
	for x in curs: 
		if x == None:
			print('Tabela vazia!')
		else:
			print(x)

select_all(mycursor,'INSCRITOS')