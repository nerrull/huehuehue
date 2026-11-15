import json
class DummyDB:
    

    def __init__(self,):
        self.room_data = self.load_room_data()
        self.dash_elements = {}

    def load_room_data(self):
        path = "./dummy_room_data.json"
        with open(path) as f:
            return json.load(f);
        return {}

    def get_rooms(self):
        return self.room_data.keys()

    def get_lights(self, room):
        return self.room_data[room]

    def set_elements_dict(self, d):
        self.dash_elements=  d
        
    def get_room_elements(self, room):
        return self.dash_elements[room]

