from flask import Flask, jsonify, make_response, request
from functools import wraps
import hashlib
import mysql.connector
import methods_sql as sql

dbapi = mysql.connector.connect(
	host='127.0.0.1',
	user='userapi',
	passwd='123456',
	database='MYBLOG'
	)

mycursor = dbapi.cursor()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# Método para autorização e autenticação na API
def auth_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if auth:
			var = sql.credentials(mycursor, auth.username)
			pswd = hashlib.sha512(str(auth.password).encode('utf-8')).hexdigest()
			if auth.username == var['User'] and pswd == var['Pwd']:
				return f(*args, **kwargs)

		return make_response('Authentication failed.', 401)

	return decorated



# Temas
@app.route('/temas', methods=['GET'])
@auth_required
def temas():
	try:
		all_temas = sql.temas_all(mycursor)
		return jsonify(all_temas), 200
	except:
		return make_response('SQL excution failed.', 500)



# Tema por id
@app.route('/temas/<int:id_tema>',methods=['GET'])
@auth_required
def tema_por_id(id_tema:int):
	try:
		tema_porid = sql.temas_ids(mycursor,id_tema)
		return jsonify(tema_porid), 200
	except:
		return make_response('SQL excution failed.', 500)



# Retorna nomes e emails dado um id de tema
@app.route('/inscritos', methods=['GET'])
@auth_required
def inscritos_tema():
	try:
		id_tema = request.args.get('id_tema', None)
		cadastros_ex = sql.inscritos_tema(mycursor,id_tema)
		return jsonify(cadastros_ex), 200
	except:
		return make_response('SQL excution failed.', 500)



if __name__ == '__main__':
	app.run(debug=True)