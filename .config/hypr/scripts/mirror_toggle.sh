#!/bin/bash

#migueldeoleiros: November 2024

#simple script that toggles a commented line, in this case for switching between extending or sharing screen in hyprland

# Set the file path and the line number to toggle
FILE="/home/miguel/.dotfiles/.config/hypr/hyprland.conf"
LINE_NUMBER=5

# Use sed to toggle the comment on the specified line
if sed -n "${LINE_NUMBER}p" "$FILE" | grep -q '^#'; then
  sed -i "${LINE_NUMBER}s/^#//" "$FILE"
else
  sed -i "${LINE_NUMBER}s/^/#/" "$FILE"
fi
