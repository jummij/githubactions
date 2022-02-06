# Kopioi aikaisempi ratkaisusi tänne. Lisää tarvittaessa myös muut ratkaisusi tiedostot.
import json

file = open('postcode_map_light.json')
data = json.load(file)
dictlist = data.items()


city = input("Kirjoita postitoimipaikka: ")
city = city.upper()

#postal_codes = []

if city in data.values():
    keys = [k for k, v in dictlist if v == city]
    print('Postinumerot: ' +  (str(sorted(keys))))
else:
    print('Tuntematon postitoimipaikka')

#Testaamista varten

def multiple_zipcodes(city: str)  -> bool:
    if len(keys) > 1:
        return True
    else:
        return False

def district_is_in_data(city: str) -> bool:
    if city in data:
        return True
    else:
        return False
