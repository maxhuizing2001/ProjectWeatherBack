from datetime import datetime,timedelta

class DateAndTime:
    """
    The DataAndTime class handels the date and time from the sensors.
    """
    def getDateAndTime(self, msg):
        """
        The getDateAndTime function get the date and time from a sensor and makes 1 variable from the date and time.

        Parameters:
        -msg: The msg from the sensor.

        Returns:
        -DateTime1: DateTime1 is the variable with the date and time in 1.
        """
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