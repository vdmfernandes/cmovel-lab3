import httplib, urllib
import sys, traceback
from time import localtime, strftime
import serial

default_string = 'Temperatura: {}, Umidade: {}'
#serial_port = '/dev/ttyUSB0'
serial_port = '/dev/ttyACM0'
def doit():

    data = ser.readline()
    temp,umid = data.split(" ")
    params = urllib.urlencode({'field1': temp, 'field2': umid, 'key':'C1PZP1GRMW1ESNN9'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")

    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print default_string.format(temp, umid)
        print strftime("%a, %d %b %Y %H:%M:%S", localtime())
        print response.status, response.reason
        readresponse = response.read()
        conn.close()
    except:
        traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    ser = serial.Serial(port=serial_port, baudrate=9600)
    while True:
        doit()
