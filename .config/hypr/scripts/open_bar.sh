#!/usr/bin/env bash

# Open bar in the main monito
# If there is only one screen open bar in that one, if there is 2 or more open it in the second one

# Get the number of monitors connected
num_monitors=$(hyprctl -j monitors | jq '. | length')

if [ $num_monitors -ge 2 ]; then
    eww open bar-main
else
    eww open bar-laptop
fi
