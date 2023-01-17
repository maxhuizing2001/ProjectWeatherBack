from datetime import datetime,timedelta

class DateAndTime:
    def getDateAndTime(self, msg):
        #Keys for getting the information
        key1 = str(msg.payload).find('received_at')
        key3 = str(msg.payload).find('uplink_message')

        #Obtaining the date and time also adjusting the time to winter daylight savings
        date = str(msg.payload)[key1 + 14: key3 - 23]
        time = str(msg.payload)[key1 + 25: key3 - 14]
        datetime1 = date + ' ' + time
        #Time adjustment for winter time
        datetime1 = datetime.strptime(datetime1, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)
        print(str(datetime1))
        return datetime1