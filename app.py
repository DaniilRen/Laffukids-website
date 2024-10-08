from flask import Flask
from flask import render_template
from yookassa import Configuration, Payment
import uuid


app = Flask(__name__)

Configuration.account_id = '467956'
Configuration.secret_key = 'test_Yf2ocwOYQBDf1P7VRXW-exqxyMmmL4Zo8BOzQsaYnWA'


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/politics')
def politics():
	return render_template('politics.html')


@app.route('/oferta')
def oferta():
	return render_template('oferta.html')\


@app.route('/payment', methods=('GET', 'POST'))
def create_payment():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		phone = request.form['phone']



if __name__ == "__main__":
	app.run(port=8090)