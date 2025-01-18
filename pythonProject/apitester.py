import requests

url = "https://free-to-play-games-database.p.rapidapi.com/api/game"

querystring = {"id":"452"}

headers = {
	"X-RapidAPI-Key": "496836dac1msh86abcf22ec16857p1cad97jsndc6df3501498",
	"X-RapidAPI-Host": "free-to-play-games-database.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)