"""
This utility generates a Selenium IDE script for adding attendees to an event on Bevy platform
"""

import copy

import serializer
import deserializer
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

    def generate_first_name_command(self, first_name):
        """
        Generates type first name command
        """
        command = copy.deepcopy(self.command_template)
        command['id'] = utils.generate_uuid()
        command['command'] = 'type'
        command['target'] = 'id=s1vcua'
        command['targets'] = [
            ["id=s1vcua", "id"],
            ["name=first_name", "name"],
            ["css=#s1vcua", "css:finder"],
            ["xpath=//input[@id='s1vcua']", "xpath:attributes"],
            ["xpath=//div[@id='overlay-container']/div/div/div[2]/form/div/div/div/div/div/input", "xpath:idRelative"],
            ["xpath=//form/div/div/div/div/div/input", "xpath:position"]
        ]
        command['value'] = first_name
        return command

    def generate_last_name_command(self, last_name):
        """
        Generates type last name command
        """
        command = copy.deepcopy(self.command_template)
        command['id'] = utils.generate_uuid()
        command['command'] = 'type'
        command['target'] = 'id=s1yx3r'
        command['targets'] = [
            ["id=s1yx3r", "id"],
            ["name=last_name", "name"],
            ["css=#s1yx3r", "css:finder"],
            ["xpath=//input[@id='s1yx3r']", "xpath:attributes"],
            ["xpath=//div[@id='overlay-container']/div/div/div[2]/form/div/div[2]/div/div/div/input", "xpath:idRelative"],
            ["xpath=//div[2]/div/div/div/input", "xpath:position"]
        ]
        command['value'] = last_name
        return command

    def generate_email_command(self, email):
        """
        Generates type email command
        """
        command = copy.deepcopy(self.command_template)
        command['id'] = utils.generate_uuid()
        command['command'] = 'type'
        command['target'] = 'id=s2v3vd'
        command['targets'] = [
            ["id=s2v3vd", "id"],
            ["name=email", "name"],
            ["css=#s2v3vd", "css:finder"],
            ["xpath=//input[@id='s2v3vd']", "xpath:attributes"],
            ["xpath=//div[@id='overlay-container']/div/div/div[2]/form/div/div[3]/div/div/div/input", "xpath:idRelative"],
            ["xpath=//div[3]/div/div/div/input", "xpath:position"]
        ]
        command['value'] = email
        return command

    def generate_save_and_add_command(self):
        """
        Generates click command for Save and Add More
        """
        command = copy.deepcopy(self.command_template)
        command['id'] = utils.generate_uuid()
        command['command'] = 'click'
        command['target'] = 'css=.Button-Button__outlined_bddio'
        command['targets'] = [
            ["css=.Button-Button__outlined_bddio", "css:finder"],
            ["xpath=(//button[@type='button'])[5]", "xpath:attributes"],
            ["xpath=//div[@id='overlay-container']/div/div/div[2]/form/div/div[6]/div/div[2]/div/button", "xpath:idRelative"],
            ["xpath=//div[2]/div/button", "xpath:position"],
            ["xpath=//button[contains(.,'Save and add more')]", "xpath:innerText"]
        ]
        return command

    def add_attendees_commands(self):
        """
        Add commands to type attendee first name, last name and email for all attendees.
        Click Save and Add More after typing
        """
        attendees_list = serializer.AttendeeCSVSerializer().get_attendees()
        for attendee in attendees_list:
            self.base['tests'][0]['commands'].append(
                self.generate_first_name_command(attendee['first_name'])
            )
            self.base['tests'][0]['commands'].append(
                self.generate_last_name_command(attendee['last_name'])
            )
            self.base['tests'][0]['commands'].append(
                self.generate_email_command(attendee['email'])
            )
            self.base['tests'][0]['commands'].append(
                self.generate_save_and_add_command()
            )

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
