from  flask import Flask 
from flask import session
from flask import request

app = Flask(__name__)
app.secret_key = "somekey"


@app.route('/',methods=['GET','POST'])
def index():
	print(session)
	session['counter'] += 0
	if request.method == "POST":
		if request.form['box'] == "1":
			session['counter'] += 1
			return "session counter = {}".format(session['counter'])
		elif request.form['box'] == "reset":
			session['counter'] = 0
			return "session counter = {}".format(session['counter'])
		else:
			return "session counter = {}".format(session['counter'])
	form = """
			<form method="POST">
			<input type="text" name="box">
			<input type="submit" name="submit_val">
			</form>
		"""
	return form


if __name__ == '__main__':
	app.run(debug=True,port=8080)