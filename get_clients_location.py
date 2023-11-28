import requests

def get_clients_location():
    
    url = "https://geo.ipify.org/api/v2/country,city?apiKey=at_BxhmiiWGsg0vO9x7XuQRec5XLVXHr"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        lat=data["location"]["lat"]
        lng= data["location"]["lng"]

        return str(lat)+", "+ str(lng)
    else:
        return {"error":"error while loading the data, please check your connection"}

