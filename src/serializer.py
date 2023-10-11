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
        return self.load_json("templates/base.json")

    def get_start_commands(self):
        """
        fetches a list of start commands
        """
        return self.load_json("templates/start_commands.json")

    def get_end_commands(self):
        """
        fetches a list of end commands
        """
        return self.load_json("templates/end_commands.json")

    def get_command_template(self):
        """
        fetches the command template
        """
        return self.load_json("templates/command.json")

    def get_config(self):
        """
        fetches the current config
        """
        return self.load_json("./config.json")

class AttendeeCSVSerializer:
    """
    Class for serializing attendess CSV list
    """

    def __init__(self):
        self.attendees = []
        with open('./samples/attendees.csv', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, skipinitialspace=True)
            headers = next(csv_reader, None)

            self.validate_file_format(headers)

            for row in csv_reader:
                self.validate_row(row)
                self.attendees.append({
                    'first_name': row[0],
                    'last_name': row[1],
                    'email' : row[2]
                })
    
    def validate_file_format(self, headers):
        """
        Validates the CSV file format
        """

        #check file data
        if(headers) == None:
            raise ValueError('The file is empty')

        #check number of columns
        if(len(headers)) != 3:
            raise ValueError('The file must have exactly three columns')
        
        #check column names
        if headers[0] != 'first_name':
            raise ValueError('The first column name must be `first_name`')
        if headers[1] != 'last_name':
            raise ValueError('The second column name must be `last_name`')
        if headers[2] != 'email':
            raise ValueError('The third column name must be `email`')

    def validate_row(self, row):
        """
        Validates the row format
        """

        #check the first and last name
        if not row[0] or not row[1]:
            raise ValueError('The first name and last name cannot be empty')

        # Check the email address
        if not re.match(r'^.+@.+\..+$', row[2]):
            raise ValueError('The email address is invalid')

    def get_attendees(self):
        """
        returns the attendees list
        """
        return self.attendees