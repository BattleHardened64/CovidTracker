from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="http")
location = geolocator.reverse("51.5074, 0.1278")

print(location.address)
