from flask import Flask, redirect, url_for, render_template, request,abort,make_response

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
	return render_template("index.html")
	
	
@app.route("/slike")
def slike():
	return render_template("slike.html")
	
@app.route("/treneri")
def treneri():
	return render_template("treneri.html")
	

@app.route("/radnoVrijeme")
def radnoVrijeme():
	return render_template("radnoVrijeme.html")


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

@app.route("/login")
def login():
	return render_template("login.html")

if __name__ == "__main__":
	app.run(debug=True)