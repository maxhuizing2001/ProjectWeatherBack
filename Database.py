import mysql.connector 
from mysql.connector.constants import ClientFlag

class Database:
    def _init_(self):
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
        #SQL Querrie to check if primary key already exists in the table
        check_query = "SELECT device_eui FROM device WHERE device_eui = %s"
        value = (listDeviceData[0],)
        self.cursor.execute(check_query, value)
        result = self.cursor.fetchone()
        if result:
            print("Primary key already exists in the table")
            return
        #SQL Querrie to insert data in database
        query = "INSERT INTO device (device_eui, device_id) VALUES (%s, %s)"
        value = (listDeviceData[0], listDeviceData[1])
        self.cursor.execute(query, value)
        self.conn.commit()

    def insertMetaDataPy(self, device_eui, Light, Pressure, datetime1, Temperature):
        #SQL Querrie to insert data in database
        sql = "INSERT INTO wheater_forecast (device_eui, date_time,temperature,temperature_inside,ambient_light,humidity,barometric_pressure) VALUES (%s,%s,%s,DEFAULT,%s,DEFAULT,%s)"
        val = (device_eui, datetime1,Temperature,Light,Pressure)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def insertMetaDataLhtSaxion(self, datetime1,device_eui,Humidity,Temp_Out,Temperature):
        #SQL Querrie to insert data in database
        sql = "INSERT INTO wheater_forecast (device_eui,date_time,temperature,temperature_inside,ambient_light,humidity,barometric_pressure) VALUES (%s,%s,%s,%s,DEFAULT,%s,DEFAULT)"
        val = (device_eui,datetime1,Temperature,Temp_Out,Humidity)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def insertMetaDataElse(self, Light,datetime1,device_eui,Humidity,Temperature):
        #SQL Querrie to insert data in database
        sql = "INSERT INTO wheater_forecast (device_eui,date_time,temperature,temperature_inside,ambient_light,humidity,barometric_pressure) VALUES (%s,%s,%s,DEFAULT,%s,%s,DEFAULT)"
        val = (device_eui,datetime1,Temperature,Light,Humidity)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def insertDevData(self, latitude, longitude, AirTime,device_eui,datetime1,RSSI):
        sqlDevMeta = "INSERT INTO device_metadata (latitude, longitude, rssi, air_time,received_at,device_eui) VALUES (%s,%s,%s,%s,%s,%s)"
        valDevMeta = (latitude, longitude,RSSI ,AirTime,datetime1,device_eui)
        self.cursor.execute(sqlDevMeta, valDevMeta)
        self.conn.commit()