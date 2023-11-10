"""
    Generates commands for scripts
"""
import copy
import utils
import serializer



class CommandGenerator:

    def __init__(self) -> None:
        serialize = serializer.JSONSerializer()
        self.commands = []
        self.command_template = serialize.get_command_template()
    
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
    
    def generate_pause_command(self, target=4000):
        """
        Generates command pausing the execution for the given number of seconds
        """
        command = copy.deepcopy(self.command_template)
        command['id'] = utils.generate_uuid()
        command['command'] = 'pause'
        command['target'] = str(target)
        return command