#!/usr/bin/env bash

#migueldeoleiros: November 2024

#simple script that moves hyprland workspaces around connected monitors

# Get the IDs of all monitors
MONITORS=$(hyprctl monitors -j | jq -r '.[] | .id')

# Get the ID of the currently focused monitor
CURRENT=$(hyprctl monitors -j | jq -r '.[] | select(.focused == true) | .id')

# Find the index of the current monitor in the list
INDEX=$(echo "$MONITORS" | tr ' ' '\n' | grep -n "$CURRENT" | cut -d: -f1)

# Calculate the index of the next monitor
NEXT_INDEX=$(( (INDEX + 1) % $(echo "$MONITORS" | wc -w) ))

# Get the ID of the next monitor
NEXT_MONITOR=$(echo "$MONITORS" | tr ' ' '\n' | head -n $((NEXT_INDEX + 1)) | tail -n 1)

# Move the current workspace to the next monitor
hyprctl dispatch movecurrentworkspacetomonitor "$NEXT_MONITOR"
