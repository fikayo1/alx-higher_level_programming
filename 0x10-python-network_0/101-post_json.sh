#!/bin/bash
# send a json POST request with arguments
curl -sH "Content-Type: application/json" -d "@$2" "$1"
