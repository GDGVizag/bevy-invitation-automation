"""
Serializer classes for json and csv files from source
"""

import json

class JSONSerializer:
    """
    Class for serializing JSON files
    """

    def load_json(self, location):
        """
        Standard method for loading JSON files
        """
        data = None
        with open(location, encoding='utf-8') as json_file:
            data = json.loads(json_file)
        if data:
            return data
        else:
            raise FileNotFoundError

    def get_base_dict(self):
        """
        fetches the base template
        """
        return self.load_json("../templates/base.json")

    def get_start_commands(self):
        """
        fetches a list of start commands
        """
        return self.load_json("../templates/start_commands.json")

    def get_end_commands(self):
        """
        fetches a list of end commands
        """
        return self.load_json("../templates/end_commands.json")

    def get_command_template(self):
        """
        fetches the command template
        """
        return self.load_json("../templates/command.json")
