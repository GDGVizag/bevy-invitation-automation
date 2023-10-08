import json

class JSONDeserializer:
    """
    Deserializes JSON and writes to file
    """

    def write_json_to_file(self, path, data):
        """
        Writes given data to file as JSON
        """
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file)