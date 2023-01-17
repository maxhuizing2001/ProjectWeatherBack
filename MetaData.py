class MetaData:

    def getDeviceData(self, msg):
        listDeviceData = []

        #Finding the eui and saving the value
        find_eui = str(msg.payload).find('dev_eui')
        find_eui2 = str(msg.payload).find('join_eui')
        device_eui = str(msg.payload)[find_eui + 10: find_eui2 - 3]
    
        #Obtaining the sensor name
        name1=(msg.topic).find('devices_id')
        name2=(msg.topic).find('application_ids')
        SensorName= str(msg.topic)[name1 + 45:name2 - 2]
        

        #Finding RSSI
        findRSSI = str(msg.payload).find('rssi')
        findRSSI2 = str(msg.payload).find('channel_rssi')
        RSSI = str(msg.payload)[findRSSI + 6:findRSSI2 - 2]
        RSSI = int(RSSI)
        listDeviceData.append(device_eui)
        listDeviceData.append(SensorName)
        listDeviceData.append(SensorName)
        listDeviceData.append(RSSI)
        print("DEVICEDATA")
        print("----------------------------------------")
        for x in listDeviceData:
            print(x, "Type: ", type(x))
        print("\n")
        return listDeviceData


    def getMetaDataPySaxWier(self, msg):
        listMetaData = []
        #Keys for getting the information
        key2 = str(msg.payload).find('rx_metadata')

        findAir = str(msg.payload).find('consumed_airtime')
        findAir2 = str(msg.payload).find('network_ids')

        #Finding the location of the data
        light = str(msg.payload).find('light')
        temperature = str(msg.payload).find('temperature')
        pressure = str(msg.payload).find('pressure')

        #Selecting the data
        Light = str(msg.payload)[light + 7: pressure - 2]
        Temperature = str(msg.payload)[temperature + 13: key2 - 3]
        Pressure = str(msg.payload)[pressure + 10: temperature - 2]
        AirTime = str(msg.payload)[findAir + 19:findAir2 -3]

        #Remove the s letter in the variable
        AirTime = AirTime.replace('s', "")

        #Convert to the right type
        Light = float(Light)
        Temperature = float(Temperature)
        Pressure = float(Pressure)
        AirTime = float(AirTime)

        #Append to list
        listMetaData.append(Light)
        listMetaData.append(Pressure)
        listMetaData.append(Temperature)
        listMetaData.append(AirTime)
        print("METADATAPYSAX")
        print("----------------------------------------")
        for x in listMetaData:
            print(x, "Type: ", type(x))
        print("\n")
        return listMetaData

    def getMetaDatalhtSax(self, msg):
        listMetaData = []

        #Keys for getting the information
        key2 = str(msg.payload).find('rx_metadata')
        findAir = str(msg.payload).find('consumed_airtime')
        findAir3 = str(msg.payload).find('version_ids')

        #Finding the location of the data
        humidity = str(msg.payload).find('Hum_SHT')
        temp_out = str(msg.payload).find('TempC_DS')
        temperature = str(msg.payload).find('TempC_SHT')

        #Selecting the data
        Temp_Out = str(msg.payload)[temp_out + 10: temperature - 2]
        Temperature = str(msg.payload)[temperature + 12: key2 - 3]
        Humidity= str(msg.payload)[humidity + 9: temp_out - 2]
        AirTime = str(msg.payload)[findAir + 19:findAir3 -3]
        
        #Remove the s letter in the variable
        AirTime = AirTime.replace('s', "")

        #Convert to the right type
        Temp_Out = float(Temp_Out)
        Temperature = float(Temperature)
        Humidity = float(Humidity)
        AirTime = float(AirTime)

        listMetaData.append(Temp_Out)
        listMetaData.append(Temperature)
        listMetaData.append(Humidity)
        listMetaData.append(AirTime)

        print("METADATALHTSAXIO")
        print("----------------------------------------")
        for x in listMetaData:
            print(x, "Type: ", type(x))
        print("\n")
        return listMetaData

    def getMetaDataElse(self, msg):
        listMetaData = []

        #Keys for getting the information
        key2 = str(msg.payload).find('rx_metadata')

        findAir = str(msg.payload).find('consumed_airtime')
        findAir3 = str(msg.payload).find('version_ids')
        #Finding the location of the data
        humidity = str(msg.payload).find('Hum_SHT')
        light = str(msg.payload).find('ILL_lx')
        temperature = str(msg.payload).find('TempC_SHT')

        #Selecting the data
        Light = str(msg.payload)[light + 8: temperature - 2]
        Temperature = str(msg.payload)[temperature + 11: key2 - 37]
        Humidity = str(msg.payload)[humidity + 9: light - 2]
        AirTime = str(msg.payload)[findAir + 19:findAir3 -3]
        
        #Remove the s letter in the variable
        AirTime = AirTime.replace('s', "")

        #Convert to the right type
        Light = float(Light)
        Temperature = float(Temperature)
        Humidity = float(Humidity)
        AirTime = float(AirTime)

        listMetaData.append(Light)
        listMetaData.append(Humidity)
        listMetaData.append(Temperature)
        listMetaData.append(AirTime)

        print("ELSE")
        print("----------------------------------------")
        for x in listMetaData:
            print(x, "Type: ", type(x))
        print("\n")
        return listMetaData