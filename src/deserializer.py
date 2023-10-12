import json
import os, os.path

class JSONDeserializer:
    """
    Deserializes JSON and writes to file
    """

    def write_json_to_file(self, path, data):
        """
        Writes given data to file as JSON
        """
        if not os.path.exists("generated/"):
         os.mkdir("generated/")
        with open(path, 'w+', encoding='utf-8') as file:
            json.dump(data, file)
