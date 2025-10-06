"""
Stock web app
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

#Create endpoint for data request
@app.route("/lookup", methods = ['GET', 'POST'])
def lookup():
	#Dictionary
	output = request.form.to_dict()
	#Use keys
	stock = output["Ticker"]
	#stock = stock ensures it can be used in the template
	return render_template('output.html', stock = stock)


if __name__=='__main__':
	app.run(debug = True)

