
from pickle import TRUE
from geopy.geocoders import Nominatim

class Location:

	#print("Data van locatie is:" +locationData+ "EINDE"+"\n")
		
	def getLocationData(self, msg):
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
		return listLocationData
