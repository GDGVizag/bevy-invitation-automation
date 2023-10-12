"""
Serializer classes for json and csv files from source
"""

import json
import csv

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
            data = json.load(json_file)
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

    def get_config(self):
        """
        fetches the current config
        """
        return self.load_json("../config.json")

class AttendeeCSVSerializer:
    """
    Class for serializing attendess CSV list
    """

    def __init__(self, csv_file_name):
        self.attendees = []
        with open('../samples/' + csv_file_name, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, skipinitialspace=True)
            next(csv_reader, None)
            for row in csv_reader:
                self.attendees.append({
                    'first_name': row[0],
                    'last_name': row[1],
                    'email' : row[2]
                })

    def get_attendees(self):
        """
        returns the attendees list
        """
        return self.attendees
