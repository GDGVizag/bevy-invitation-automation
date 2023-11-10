"""
This utility generates a Selenium IDE script for adding attendees to an event on Bevy platform
"""

import serializer
import deserializer
import utils

import command_generator

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

        self.command_generator = command_generator.CommandGenerator()

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
        Click Save and Add More after typing
        """
        attendees_list = serializer.AttendeeCSVSerializer().get_attendees()
        for attendee in attendees_list:
            self.base['tests'][0]['commands'].append(
                self.command_generator.generate_first_name_command(attendee['first_name'])
            )
            self.base['tests'][0]['commands'].append(
                self.command_generator.generate_last_name_command(attendee['last_name'])
            )
            self.base['tests'][0]['commands'].append(
                self.command_generator.generate_email_command(attendee['email'])
            )
            self.base['tests'][0]['commands'].append(
                self.command_generator.generate_save_and_add_command()
            )
            self.base['tests'][0]['commands'].append(
                self.command_generator.generate_pause_command()
            )
        print("Generated script to add", len(attendees_list), "attendees.")

    def add_end_commands(self):
        """
        Appends end commands to the end of the commands list
        """
        self.base['tests'][0]['commands'] += self.end_commands

    def generate_script(self):
        """
        generates the .side script for Selenium IDE
        """
        deserialize = deserializer.JSONDeserializer()
        deserialize.write_json_to_file("generated/sample.side", self.base)

if __name__ == '__main__':
    Main()
