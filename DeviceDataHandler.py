import paho.mqtt.client as mqtt
from Location import Location
from Database import Database
from DateAndTime import DateAndTime
from MetaData import MetaData

class DeviceDataHandler:
    """
    Handles all the data received from the IoT devices, processes it and stores it in a database.
    """
    def __init__(self):
        """
        Initializes instances of the Location, MetaData, Database, and DateAndTime classes.
        """
        self.location = Location()
        self.metaData = MetaData()
        self.database = Database()
        self.dateAndTime = DateAndTime()

    
    def on_connect(self, client, userdata, flags, rc):
        """
        Callback function for when the client connects to the MQTT broker.
        Subscribes to the topics for the different devices.
        
        Parameters:
        - client (mqtt.Client) : the MQTT client instance
        - userdata: user defined data
        - flags: response flags sent by the broker
        - rc: the result code of the connection attempt
        """
        print("Connected with result code " + str(rc))
        client.subscribe("v3/project-software-engineering@ttn/devices/py-wierden/up")
        client.subscribe("v3/project-software-engineering@ttn/devices/py-saxion/up")
        client.subscribe("v3/project-software-engineering@ttn/devices/lht-wierden/up")
        client.subscribe("v3/project-software-engineering@ttn/devices/lht-gronau/up")
        client.subscribe("v3/project-software-engineering@ttn/devices/lht-saxion/up")
    
    def on_message(self, client, userdata, msg):
        """
        Callback function for when a message is received on one of the subscribed topics.
        Processes the data in the message and stores it in the database.
        
        Parameters:
        - client (mqtt.Client) : the MQTT client instance
        - userdata: user defined data
        - msg (mqtt.MQTTMessage) : the MQTT message object
        """
        listLatAndLong = self.location.getLocationData(msg)
        deviceData = self.metaData.getDeviceData(msg)
        self.database.insertDeviceData(deviceData)
        sensorName = deviceData[1]
        print(sensorName)

        _dateAndTime = self.dateAndTime.getDateAndTime(msg)

        if sensorName == 'py-saxion' or sensorName == 'py-wierden':
            metaDataPySax = self.metaData.getMetaDataPySaxWier(msg)
            airTime = metaDataPySax[3]
            self.database.insertMetaDataPy(deviceData[0], _dateAndTime, metaDataPySax[2], metaDataPySax[0], metaDataPySax[1])
        
        elif sensorName == 'lht-saxion':
            metaLHTSaxion = self.metaData.getMetaDatalhtSax(msg)
            airTime = metaLHTSaxion[3]
            self.database.insertMetaDataLhtSaxion(deviceData[0], _dateAndTime, metaLHTSaxion[1], metaLHTSaxion[0], metaLHTSaxion[2])
        
        else:
            otherDevices = self.metaData.getMetaDataElse(msg)
            airTime = otherDevices[3]
            self.database.insertMetaDataElse(deviceData[0], _dateAndTime, otherDevices[2], otherDevices[0], otherDevices[1])
        
        self.database.insertDevData(listLatAndLong[0], listLatAndLong[1], airTime, deviceData[0], _dateAndTime, deviceData[3])

def main():
    """
    The main function of the script.
    Creates an instance of the DeviceDataHandler class and sets up the MQTT client callbacks.
    Connects to the MQTT broker and runs the client's main loop indefinitely.
    """
    client = mqtt.Client()
    device_data_handler = DeviceDataHandler()
    client.on_connect =device_data_handler.on_connect
    client.on_message = device_data_handler.on_message
    client.username_pw_set('project-software-engineering@ttn', 'NNSXS.DTT4HTNBXEQDZ4QYU6SG73Q2OXCERCZ6574RVXI.CQE6IG6FYNJOO2MOFMXZVWZE4GXTCC2YXNQNFDLQL4APZMWU6ZGA')
    client.connect("eu1.cloud.thethings.network", 1883, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()