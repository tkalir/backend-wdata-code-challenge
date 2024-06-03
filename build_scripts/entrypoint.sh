#!/bin/bash

./build_scripts/wait-for-db.sh db

# Check if the flag file exists
if [ ! -f /var/run/first_start_complete ]; then
    # Run the first start script
    ./build_scripts/first_start.sh
fi

echo "Received arguments: $@"
# Continue with the default command
exec "$@"