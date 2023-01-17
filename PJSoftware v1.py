#Robert Alexandru Calin 479454 v1

from sqlite3 import Cursor
import paho.mqtt.client as mqtt
from Location import Location
from Database import Database
from DateAndTime import DateAndTime
from MetaData import MetaData


def main():
    #The next section subscribes to the individual sensor 
    # and anounces the conection with a conection code that should be 0 for a good connection

    location = Location()
    metaData = MetaData()
    database = Database()
    dateAndTime = DateAndTime()

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("v3/project-software-engineering@ttn/devices/py-wierden/up")
        client.subscribe("v3/project-software-engineering@ttn/devices/py-saxion/up")
        client.subscribe("v3/project-software-engineering@ttn/devices/lht-wierden/up")
        client.subscribe("v3/project-software-engineering@ttn/devices/lht-gronau/up")
        client.subscribe("v3/project-software-engineering@ttn/devices/lht-saxion/up")
    
    #This section takes the received payload and searches for specific fields 
    # formats the payload and shows the individual values for each sensor and the meaning of the value
    #Also not all sensors have presure some have humidity so it also check wich of the two
    def on_message(client, userdata, msg):

        #location program
        listLatAndLong = location.getLocationData(msg)

        deviceData = metaData.getDeviceData(msg)
        database.insertDeviceData(deviceData)
        sensorName = deviceData[1]
        print(sensorName)

        _dateAndTime = dateAndTime.getDateAndTime(msg)

        if sensorName == 'py-saxion' or sensorName == 'py-wierden':
            metaDataPySax = metaData.getMetaDataPySaxWier(msg)
            airTime = metaDataPySax[3]
            database.insertMetaDataPy(metaDataPySax[0], metaDataPySax[1], _dateAndTime, deviceData[0], metaDataPySax[2])
        
        elif sensorName == 'lht-saxion':
            metaLHTSaxion = metaData.getMetaDatalhtSax(msg)
            airTime = metaLHTSaxion[3]
            database.insertMetaDataLhtSaxion(_dateAndTime, deviceData[0], metaLHTSaxion[0], metaLHTSaxion[1], metaLHTSaxion[2])
        
        else:
            otherDevices = metaData.getMetaDataElse(msg)
            airTime = otherDevices[3]
            database.insertMetaDataElse(otherDevices[0], _dateAndTime, deviceData[0], otherDevices[1], otherDevices[2])
        
        database.insertDevData(listLatAndLong[0], listLatAndLong[1], airTime, deviceData[0], _dateAndTime, deviceData[3])


    #This section conects using the needed username and pasword
    #also initializes the conection and formating of the payload
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set('project-software-engineering@ttn', 'NNSXS.DTT4HTNBXEQDZ4QYU6SG73Q2OXCERCZ6574RVXI.CQE6IG6FYNJOO2MOFMXZVWZE4GXTCC2YXNQNFDLQL4APZMWU6ZGA')
    client.connect("eu1.cloud.thethings.network", 1883, 60)

    #The loop cheking for new payload and after formating prints the needed information
    client.loop_forever()
    print(client.on_message)

if __name__ == "__main__":
    main()