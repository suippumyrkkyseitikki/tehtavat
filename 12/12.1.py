import requests


pyyntö = requests.get("https://api.chucknorris.io/jokes/random")
data = pyyntö.json()


print(data["value"])
