from flask import Flask
from flask import render_template as render,url_for
import requests as r
app = Flask(__name__)


#I2C Pins 
#GPIO2 -> SDA
#GPIO3 -> SCL

#Import the Library Requreid 
import smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
#Slave Address 1
address = 0x66

#Slave Address 2
address_2 = 0x66

def writeNumber(value):
    bus.write_byte(address, value)
    bus.write_byte(address_2, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    # number = bus.read_byte(address)
    number = bus.read_byte_data(address, 1)
    return number
    
# while True:
#     #Receives the data from the User
#     data = input("Enter the data to be sent : ")
#     data_list = list(data)
#     for i in data_list:
#         #Sends to the Slaves 
    #     writeNumber(int(ord(i)))
    #     time.sleep(.1)

    # writeNumber(int(0x0A))

@app.route('/')
def hello():
	api = r.get('https://feeds.divvybikes.com/stations/stations.json')
	data = api.json()
	station = data['stationBeanList'][45]['stationName']
	docks = data['stationBeanList'][45]['availableDocks']
	bikes = data['stationBeanList'][45]['availableBikes']
	return render("index.html",docks=docks,station=station,bikes=bikes)


@app.route('/red')
def red():
	writeNumber(int(ord('1')))
	time.sleep(.1)
	writeNumber(int(0x0A))
	return None







if __name__ == '__main__':
	app.run(debug=True,static_url_path='static')