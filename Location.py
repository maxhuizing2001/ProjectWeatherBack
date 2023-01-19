class Location:
	"""
	Location class gets the location data from the sensors.
	"""
	def getLocationData(self, msg):
		"""
		The getLocationData gets the latitude and longitude the message that is passed to the funciton.

		Parameters:
		- msg: raw data from the sensor.

		Returns:
		-List with latitude and longitude.
		"""
		listLocationData = []
		locationReferenceBegin = str(msg.payload).find('location')
		locationReferenceEnd = str(msg.payload).find('source')
		locationData = str(msg.payload)[locationReferenceBegin:locationReferenceEnd+6]

		if locationData.__contains__('altitude'):
			latitudeReference = locationData.find('latitude')
			longitudeReference = locationData.find('longitude')
			altitudeReference = locationData.find('altitude')
			latitude = locationData[latitudeReference+10:longitudeReference-2]
			longitude = locationData[longitudeReference+11:altitudeReference-2]
		else:
			latitudeReference = locationData.find('latitude')
			longitudeReference = locationData.find('longitude')
			sourceReference = locationData.find('source')
			latitude = locationData[latitudeReference+10:longitudeReference-2]
			longitude = locationData[longitudeReference+11:sourceReference-2]

		listLocationData.append(latitude)
		listLocationData.append(longitude)
		print(latitude)
		print(longitude)
		return listLocationData
