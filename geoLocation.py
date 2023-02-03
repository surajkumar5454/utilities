# importing geopy library
from geopy.geocoders import Nominatim

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# entering the location name
getLoc = loc.geocode("248001")

# printing address
print(getLoc.address)

# printing latitude and longitude
print("Latitude = ", getLoc.latitude)
print("Longitude = ", getLoc.longitude)

# # Importing required module
# from geopy.geocoders import Nominatim
#
# # Using Nominatim Api
# geolocator = Nominatim(user_agent="geoapiExercises")
#
# # Zipcode input
# zipcode = "110022"
#
# # Using geocode()
# location = geolocator.geocode(zipcode)
#
# # Displaying address details
# print("Zipcode:", zipcode)
# print("Details of the Zipcode:")
# print(location)