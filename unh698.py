from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello UNH698 Website!'

@app.route('/')
def index_page():
	return 'This is the Main Page'

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=8080)	
