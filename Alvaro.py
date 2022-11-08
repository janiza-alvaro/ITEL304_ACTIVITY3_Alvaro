from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
	return """
		<html><body style="margin-top:20%;">
			<h1 style="font-size:60px; text-align: center;">Hi im janiza, Iza for short!</h1>
			<p style="font-size:40px; text-align: center;">The date and time is {0}</p>
		</body></html>
		""".format(str(datetime.now()))

app.run(host="localhost", debug=True)
