from email.policy import default
from turtle import width
from unittest.mock import DEFAULT
import mysql.connector 
from mysql.connector.constants import ClientFlag

class Database:
    def __init__(self):
        config = {
            'user': 'u1656_BotTzlvfQc',
            'password': '8J9NeEVFXAIEY+2Jn+^8@sWn',
            'host': 'database.discordbothosting.com',
            'database': 's1656_projectWeather',
            'client_flags': [ClientFlag.SSL],
            'ssl_ca': 'server-ca.pem',
            'ssl_cert': 'client-cert.pem',
            'ssl_key': 'client-key.pem'
            }
        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()
        if self.conn.is_connected():
            print("succes")

    def insertDeviceData(self, listDeviceData):
        #SQL Querrie to insert data in database
        sqlDevice = "INSERT INTO device (device_eui,device_id) VALUES (?,?)"
        valDevice = (listDeviceData[0],listDeviceData[1])
        self.cursor.execute(sqlDevice, valDevice)
        self.conn.commit()

    def insertMetaDataPy(self, Light, Pressure, datetime1, device_eui, Temperature):
        #SQL Querrie to insert data in database
        sql = "INSERT INTO wheater_forecast (device_eui,date_time,temperature,temperature_inside,ambient_light,humidity,barometric_pressure) VALUES (?,?,?,DEFAULT,?,DEFAULT,?)"
        val = (device_eui,datetime1,Temperature,default ,Light,default,Pressure)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def insertMetaDataLhtSaxion(self, datetime1,device_eui,Humidity,Temp_Out,Temperature):
        #SQL Querrie to insert data in database
        sql = "INSERT INTO wheater_forecast (device_eui,date_time,temperature,temperature_inside,ambient_light,humidity,barometric_pressure) VALUES (?,?,?,?,DEFAULT,?,DEFAULT)"
        val = (device_eui,datetime1,Temperature,Temp_Out, default,Humidity, default)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def insertMetaDataElse(self, Light,datetime1,device_eui,Humidity,Temperature):
        #SQL Querrie to insert data in database
        sql = "INSERT INTO wheater_forecast (device_eui,date_time,temperature,temperature_inside,ambient_light,humidity,barometric_pressure) VALUES (?,?,?,DEFAULT,?,?,DEFAULT)"
        val = (device_eui,datetime1,Temperature, default,Light,Humidity, default)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def insertDevData(self, latitude, longitude, AirTime,device_eui,datetime1,RSSI):
        sqlDevMeta = "INSERT INTO device_metadata (latitude, longitude, rssi, air_time,received_at,device_eui) VALUES (?,?,?,?,?,?)"
        valDevMeta = (latitude, longitude,RSSI ,AirTime,datetime1,device_eui)
        self.cursor.execute(sqlDevMeta, valDevMeta)
        self.conn.commit()