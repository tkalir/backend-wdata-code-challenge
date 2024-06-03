#!/bin/bash

# Commands to be executed only once
python -m code.main read-data input_data

# Create a flag file to indicate that the script has run
touch /var/run/first_start_complete
