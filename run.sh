#!/bin/bash

PYTHON=/usr/bin/python

# Move into the source directory.
pushd flatland
# Build.
make
# Run a simple HTTP server for the app.
$PYTHON -m SimpleHTTPServer &
# Save the pid of the server and kill it on exit.
pid=$!
trap "kill $pid" SIGINT SIGTERM EXIT
google-chrome --incognito http://localhost:8000/
wait $!
popd
