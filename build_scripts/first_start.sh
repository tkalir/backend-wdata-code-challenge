#!/bin/bash

# Commands to be executed only once
python ./code/main.py read-data input_data

# Create a flag file to indicate that the script has run
touch /var/run/first_start_complete
