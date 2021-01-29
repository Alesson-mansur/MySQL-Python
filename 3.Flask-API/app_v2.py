from flask import Flask, jsonify, make_response, request
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

# Home
#@app.route('/')
#def home():
#	return '<h1>My first app!</h1>'


# Temas
@app.route('/temas', methods=['GET'])
def temas():
	try:
		all_temas = sql.temas_all(mycursor)
		return jsonify(all_temas), 200
	except:
		return make_response('SQL excution failed.', 500)


# Tema por id
@app.route('/temas/<int:id_tema>',methods=['GET'])
def tema_por_id(id_tema:int):
	try:
		tema_porid = sql.temas_ids(mycursor,id_tema)
		return jsonify(tema_porid), 200
	except:
		return make_response('SQL excution failed.', 500)


# Retorna nomes e emails dado um id de tema
@app.route('/inscritos', methods=['GET'])
def inscritos_tema():
	try:
		id_tema = request.args.get('id_tema', None)
		cadastros_ex = sql.inscritos_tema(mycursor,id_tema)
		return jsonify(cadastros_ex), 200
	except:
		return make_response('SQL excution failed.', 500)


if __name__ == '__main__':
	app.run(debug=True)