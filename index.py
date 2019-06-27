from flask import Flask
from flask import render_template as render,url_for
import requests as r
app = Flask(__name__)

@app.route('/')
def hello():
	api = r.get('https://feeds.divvybikes.com/stations/stations.json')
	data = api.json()
	station = data['stationBeanList'][45]['stationName']
	docks = data['stationBeanList'][45]['availableDocks']
	bikes = data['stationBeanList'][45]['availableBikes']
	return render("index.html",docks=docks,station=station,bikes=bikes)






if __name__ == '__main__':
	app.run(debug=True,static_url_path='static')