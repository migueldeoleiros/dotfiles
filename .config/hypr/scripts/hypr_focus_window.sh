#!/usr/bin/env bash

# Get a list of windows in hyprland and select one to move focus
# Inspired to work similar to emacs buffers

clients=$(hyprctl -j clients)

window=$(echo "$clients" |
    jq -r '.[] | select(.class != "" ) | "[\(.workspace.name)] \(.class) - \(.title)"' |
    sort |
    rofi -dmenu -i  -p "Select window")

address=$(echo "$clients" |
    jq -r --arg win "$window" '.[] | select(.class != "" and "[\(.workspace.name)] \(.class) - \(.title)" == $win) | .address')

echo $window

hyprctl dispatch focuswindow address:$address
