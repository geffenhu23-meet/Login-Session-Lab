from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session
# login_session = {}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST']) # What methods are needed?
def home():
	if request.method == 'POST':
		try:
			login_session["quote"]= request.form["quote"]
			login_session["author"]= request.form["author"]
			login_session["age"]= request.form["age"]
			return render_template('thanks.html')
		except:
			return redirect(url_for('error'))
	else:
		return render_template('home.html')
		


# @app.route('/home')
# def home():
# try:
# 		user = login_session['user']
# 		return render_template('home.html')
# 	except:
# 		print('the key user isn’t in login_session')
# 		return redirect(url_for('login'))

	# 	if username == 'admin':
	# 	   login_session['admin'] = True
	# return render_template('home.html')

# @app.route('/manage')
# def manage():
#    if 'admin' in login_session:
#        if login_session['admin'] == True:
#            return render_template("manage.html")
#    return redirect(url_for('admin'))


@app.route('/error')
def error():
	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html',quote=quote,author=author, age=age)# What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True, port=1112)