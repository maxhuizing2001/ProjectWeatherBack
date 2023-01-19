from email.policy import default
import mysql.connector 
from mysql.connector.constants import ClientFlag

class Database:
    """
    The Database makes the connection with database and insert the data collected from the sensors.
    """
    def __init__(self):
        """
        The __init__ function is called when database object is created in the DeviceDataHandler class. It makes an connection with the database.
        """
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
        """
        The insertDeviceData function inserts the data passed in the list. Before inserting the data it checks if the device is already in the database. If the device is already in the database it ends the function and if its not in the database it adds the new device the database.

        Parameters:
        - listDeviceData: List with the data that has to be stored in the database.
        """
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

    def insertMetaDataPy(self, device_eui,datetime1, Temperature, Light, Pressure):
        """
        The insertMetaDataPy function inserts the data passed in the list.

        Parameters:
        - device_eui: The eui from the sensor.
        - datetime1: Date and time from when the data was collected from the sensor.
        - Temperature: Temperature data from the sensor.
        - Light: Light data from the sensor.
        - Pressure: Pressure data from the sensor.
        """
        #SQL Querrie to insert data in database
        sql = "INSERT INTO weather_forecast (device_eui, date_time,temperature,temperature_inside,ambient_light,humidity,barometric_pressure) VALUES (%s,%s,DEFAULT,%s,%s,DEFAULT,%s)"
        val = (device_eui, datetime1,Temperature,Light,Pressure)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def insertMetaDataLhtSaxion(self, device_eui,datetime1,Temp_Out,Temperature,Humidity):
        """
        The insertMetaDataLhtSaxion function inserts the data passed in the list.

        Parameters:
        - device_eui: The eui from the sensor.
        - datetime1: Date and time from when the data was collected from the sensor.
        - Temp_Out: Temperature outside data from the sensor.
        - Temperature: Temperature data from the sensor.
        - Humidity: Humidity data from the sensor.
        """
        #SQL Querrie to insert data in database
        sql = "INSERT INTO weather_forecast (device_eui,date_time,temperature,temperature_inside,ambient_light,humidity,barometric_pressure) VALUES (%s,%s,%s,%s,DEFAULT,%s,DEFAULT)"
        val = (device_eui,datetime1,Temperature,Temp_Out,Humidity)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def insertMetaDataElse(self, device_eui,datetime1,Temperature_out, Light, Humidity):
        """
        The insertMetaDataElse function inserts the data passed in the list.

        Parameters:
        - device_eui: The eui from the sensor.
        - datetime1: Date and time from when the data was collected from the sensor.
        - Temperature_out: Temperature outside data from the sensor.
        - Light: Light data from the sensor.
        - Humidity: Humidity data from the sensor.
        """
        #SQL Querrie to insert data in database
        sql = "INSERT INTO weather_forecast (device_eui,date_time,temperature,temperature_inside,ambient_light,humidity,barometric_pressure) VALUES (%s,%s,%s,DEFAULT,%s,%s,DEFAULT)"
        val = (device_eui,datetime1,Temperature_out,Light,Humidity)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def insertDevData(self, latitude, longitude, AirTime,device_eui,datetime1,RSSI):
        """
        The insertDevData function inserts the data passed in the list.

        Parameters:
        - latitude: Latitude from the antenna that the sensor is connected to.
        - longitude: longitude from the antenna that the sensor is connected to.
        - AirTime: Airtime data from the sensor.
        - device_eui: The eui from the sensor.
        - datetime1: Date and time from when the data was collected from the sensor.
        - RSSI: RSSI from the sensor.
        """
        if ~bool(latitude) or ~bool(longitude):
            return

        sqlDevMeta = "INSERT INTO device_metadata (latitude, longitude, rssi, air_time,received_at,device_eui) VALUES (%s,%s,%s,%s,%s,%s)"
        valDevMeta = (latitude, longitude,RSSI ,AirTime,datetime1,device_eui)
        self.cursor.execute(sqlDevMeta, valDevMeta)
        self.conn.commit()