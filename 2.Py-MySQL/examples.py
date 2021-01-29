# Inserção no banco usando o python
# Atenção ao problema SQL Injection (ver no google)
sql = 'INSERT INTO INSCRITOS (NOME, EMAIL, TELEFONE) VALUES (%s, %s, %s)'
val = ('John Locke', 'highway2@locke.com', '19 88945 6110')

mycursor.execute(sql, val)
# Comando que envia, de fato, as alterações para o banco
dbapi.commit()

# Método básico de SELECT * FROM
def select_all(curs,table:str):
	sql = 'SELECT * FROM {}'.format(table)
	curs.execute(sql)
	for x in curs: 
		if x == None:
			print('Tabela vazia!')
		else:
			print(x)

select_all(mycursor,'INSCRITOS')