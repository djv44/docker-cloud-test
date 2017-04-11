from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello_world():
	return 'Hello UNH698 Website!'

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=8080)	