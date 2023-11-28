import requests

def get_weather_data(q):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q":q,"days":"3"}

    headers = {
        "X-RapidAPI-Key": "a9a39eb820msh2212a899c6638e4p1afd4djsne466da8a1582",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()