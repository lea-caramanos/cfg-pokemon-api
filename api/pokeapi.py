import random
import requests

# Get pokemon's info via the API
def get_random_pokemon_api():
    pokemon_id = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)
    return response.json()
