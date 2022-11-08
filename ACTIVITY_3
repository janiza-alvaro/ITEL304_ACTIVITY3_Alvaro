from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
	return """
		<html>
                    <head>
                        <style>
                            body{
                                margin-top:5%;
                                margin-left:20%;
                                background:#8A8A8A;
                            }
                            h1{
                                color:#B3E5F2;
                                font-size:50px;
                                margin-left:150px;
                            }
                            form{
                                background: rgba(196, 156, 255, 0.5);
                                width: 760px;
                                height: 350px;
                                padding-left: 50px;
                                padding-top: 20px;
                                padding-bottom: 75px;
                            }
                            p{
                                font-size:35px;
                                color:#FFFFFF;
                                padding-left: 150px;
                            }
                            input{
                                font-size:20px;
                                margin-left: 150px;
                            }
                        </style>
                    </head>
                    <body >
                        <h1>Please answer the blanks</h1>
                            <form action='/show'>
                                <p>First Name</p>
                                <input type='text' name='fname' required><br><br>
                                <p>Last Name</p>
                                <input type='text' name='lname' required><br><br><br>
                                <input type='submit' value='Submit'>
                            </form>
                    </body>
            </html>
           """

@app.route('/show')
def show():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    time = str(datetime.now())
    return """
        <html><body style="background:#ADD8E6;"> 
            <div style="margin-top:20%; margin-left:30%; background:#C49CFF; width: 500px; height: 200px; padding: 15px; box-shadow: 10px 10px 5px #9CE9FF;">
                <p style="text-align:center; font-size:50px;">Hi, {0} {1}!<p>
                <p style="text-align:center; font-size:25px; margin-top:-50px">The time right now is {2}<p><br><br><br>
                <form action='/'>
                    <input type='submit' value='Back to Form'>
                </form>
                <br>
            </div>
        </body> </html>
           """.format(fname, lname, time)

app.run(host="localhost", debug=True)
