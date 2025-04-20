#!/bin/bash

#migueldeoleiros: April 2025

# simple script that provides a menu for selecting display configurations in hyprland
# this script could be easily tweaked for other kinds of selectable configurations
# thanks to hyprland autoloading, the configuration will change on the fly

CONFIG_DIR="$HOME/.config/hypr/screen_conf"

declare -A OPTIONS=(
  ["Custom Three Monitors"]="custom_three.conf"
  ["Mirror Display"]="mirror.conf"
  ["Screen on Left"]="screen_on_left.conf"
  ["Screen on Right"]="screen_on_right.conf"
)

# Use rofi to display a menu
SELECTED_TEXT=$(printf "%s\n" "${!OPTIONS[@]}" | rofi -dmenu -p "Select screen configuration:")

# Check if a selection was made
if [[ -n "$SELECTED_TEXT" ]]; then
  # Get the corresponding file name from the associative array
  SELECTED_FILE="${OPTIONS[$SELECTED_TEXT]}"

  SOURCE_LINE="source = $CONFIG_DIR/$SELECTED_FILE"
  echo "$SOURCE_LINE" > "$CONFIG_DIR/screen.conf"
fi
