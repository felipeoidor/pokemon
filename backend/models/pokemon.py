from backend.api_client import get_data

class Pokemon():
    def __init__ (self, identifier):
        data = get_data(identifier)
        self.id = data["id"]
        self.name = data["name"].capitalize()
        self.types = [type["type"]["name"].capitalize() for type in data["types"]]
        self.sprite = data["sprites"]["front_default"]