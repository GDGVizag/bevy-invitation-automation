# Bevy Invite Automation Script Generator

Generates a Selenium Automation script (.side) for adding attendees to a Bevy Event.

Tested on:
1. Chrome

To generate a script for a particular event, update the following files with the respective data:
 1. [config.js](config.json)
    `"event_id"`: "event-`XXXX`",
    `"event_name"`: "`event-name-on-bevy`"
2. [templates/start_commands.json](templates/start_commands.json)
    `"target"`: "/accounts/dashboard/#/chapter-318/event-`XXXXX`/manage",
