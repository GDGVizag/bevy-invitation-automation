"""
This utility generates a Selenium IDE script for adding attendees to an event on Bevy platform
"""

import json

import serializer
import utils

# Serialize the contents of base.json into a dictionary
class Main:
    """
    Driver class
    """

    def __init__(self) -> None:
        serialize = serializer.JSONSerializer()
        self.base = serialize.get_base_dict()
        self.command_template = serialize.get_command_template()
        self.start_commands = serialize.get_start_commands()
        self.end_commands = serialize.get_end_commands()
        self.config = serialize.get_config()

        self.base['id'] = utils.generate_uuid()
        self.base['name'] = self.config['event_name']
        self.base['url'] = "https://gdg.community.dev"
        self.base['tests'][0]['id'] = utils.generate_uuid()
        self.base['suites'][0]['id'] = utils.generate_uuid()
        self.base['suites'][0]['tests'] = [self.base['tests'][0]['id']]
        self.base['urls'] = ["https://gdg.community.dev"]
        
        self.set_start_commands()
        self.add_attendees_commands()
        self.add_end_commands()
        self.generate_script()

    def set_start_commands(self):
        """
        Sets test commands to start commands in the base object
        """
        self.base['tests'][0]['commands'] = self.start_commands

    def add_attendees_commands(self):
        """
        Add commands to type attendee first name, last name and email for all attendees.
        Click Save and Add More after typiing
        """
        # TODO: Load the csv file (load the specified file or load the default csv file)

    def add_end_commands(self):
        """
        Appends end commands to the end of the commands list
        """
        self.base['tests'][0]['commands'] += self.end_commands

    def generate_script(self):
        """
        generates the .side script for Selenium IDE
        """
        with open("generated/sample.side", 'w', encoding='utf-8') as file:
            json.dump(self.base, file)


if __name__ == '__main__':
    Main()
