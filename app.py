from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/bloco-de-notas')
def bloco_de_notas():
	return render_template('blocodenotas.html')

if __name__ == '__main__':
	app.run(debug=True)