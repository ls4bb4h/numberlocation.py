import phonenumbers
import folium
from phonenumbers import geocoder

print('''



               ____  _  _   ____  ____  _  _   _   _ 
              / ___|| || | | __ )| __ )| || | | | | |
              \___ \| || |_|  _ \|  _ \| || |_| |_| |
               ___) |__   _| |_) | |_) |__   _|  _  |
              |____/   |_| |____/|____/   |_| |_| |_|

  _______________________________________________________________________
 /                                                                       \ 
 \_______________________________________________________________________/

 _   _                 _               _                    _   _             
| \ | |_   _ _ __ ___ | |__   ___ _ __| |    ___   ___ __ _| |_(_) ___  _ __  
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__| |   / _ \ / __/ _` | __| |/ _ \| '_ \ 
| |\  | |_| | | | | | | |_) |  __/ |  | |__| (_) | (_| (_| | |_| | (_) | | | |
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|  |_____\___/ \___\__,_|\__|_|\___/|_| |_|
                                                                              






''')

### Telefon Numarasının Ülke Kısmı 
print("[!] Please Do Not Forget To Write The Country Code Before Entering The Phone Number [!]")

number = input("[!] Please Enter the Phone Number You Want To Find The Location [!] : ")

Key = '5f9895bf78b246a4b13eae8d1a2c865b'

samNumber = phonenumbers.parse(number)

target_number_location = geocoder.description_for_number(samNumber, "en")
print(target_number_location)

### Telefon Numarasının Operatör Kısmı 

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

### Telefon Numarasının Konum Kısmı 

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(target_number_location)

results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat, lng)

mymap = folium.Map(Location =[lat, lng], zoom_start = 9)

folium.Marker([lat, lng], popup = target_number_location).add_to((mymap))

mymap.save("target_number_location.html")
