import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "2lKKcVbPPG0vf4bm9CkYAiHHO95XAvMz"

while True:
   orig = input("Ciudad de Origen: ")
   if orig == "Salir" or orig == "s":
        break
   dest = input("Ciudad de Destino: ")
   if dest == "Salir" or dest == "s":
        break

   url = main_api + urllib.parse.urlencode ({"key" :key, "from" :orig, "to" :dest}) 
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data ["info"] ["statuscode"]
   if json_status == 0: 
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.1f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
           print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
