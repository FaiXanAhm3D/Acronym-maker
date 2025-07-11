from geopy.geocoders import ArcGIS

geolocator=ArcGIS() #initialize ArcGIS geocoder

location=geolocator.geocode("Kolkata,India")

print("Latitude:",location.latitude)
print("Longitude:",location.longitude)

location = geolocator.geocode("Barrackpore Kolkata")
print(location.address)