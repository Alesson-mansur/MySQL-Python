from flask import Flask

app = Flask(__name__)

# Home
@app.route('/', methods=['GET'])
def home():
	return '<h1>My first app!</h1>'


if __name__ == '__main__':
	app.run(debug=True)