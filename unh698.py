from flask import Flask, render_template
app = Flask(__name__)

from prometheus_metrics import setup_metrics
setup_metrics(app)

@app.route('/')
def home():
	return render_template('index.html')
	#return "UNH698 Website"

@app.route('/main')
def main():
	return render_template('main.html')

@app.route('/my-topic')
def topic():
	return render_template('topic.html')

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=8080)	