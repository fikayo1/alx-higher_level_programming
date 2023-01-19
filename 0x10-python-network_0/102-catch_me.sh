#!/bin/bash
# makes a request causing the server respond with "You got me"
curl -sL -H "Origin: School" -X "PUT" "0.0.0.0:5000/catch_me"
