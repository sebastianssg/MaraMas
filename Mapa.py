# KEY = 6kHMSpMIf5uAAbZHkwSkSf8XxEAjKjdI

# import requests module
import requests


KEY = "6kHMSpMIf5uAAbZHkwSkSf8XxEAjKjdI"
FROM = input("Ciudad de origen: ")
TO = input("Ciudad de destino: ")
TYPE = input("Tipo de ruta (fastest, shortest, pedestrian, multimodal, bicycle): ")


URL = "https://www.mapquestapi.com/directions/v2/route?key="+KEY+"&from="+FROM+"&to="+TO+"&outFormat=json&ambiguities=ignore&routeType="+TYPE+"&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false"



response = requests.get(URL)
print(response.status_code)

print(response.json())


