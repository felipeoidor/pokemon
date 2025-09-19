import requests

def get_data(identifier):
    url = f"https://pokeapi.co/api/v2/pokemon/{identifier}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return "Pokémon not found..."