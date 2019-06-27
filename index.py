from flask import Flask
from flask import render_template as render
import requests
app = Flask(__name__)

@app.route('/')
def hello():
    return render("index.html")






if __name__ == '__main__':
	app.run(debug=True)