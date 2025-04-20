#!/usr/bin/env bash

#migueldeoleiros: November 2024

#simple script that moves hyprland workspaces around connected monitors

# Get the IDs of all monitors
MONITORS=$(hyprctl monitors -j | jq -r '.[] | .id')
echo "Monitors: $MONITORS"

# Get the ID of the currently focused monitor
CURRENT=$(hyprctl monitors -j | jq -r '.[] | select(.focused == true) | .id')
echo "Current Monitor: $CURRENT"

# Find the index of the current monitor in the list
INDEX=$(echo "$MONITORS" | tr ' ' '\n' | grep -n "$CURRENT" | cut -d: -f1)
echo "Index: $INDEX"

# Calculate the index of the next monitor
NEXT_INDEX=$(( (INDEX) % $(echo "$MONITORS" | wc -w) ))
echo "Next Index: $NEXT_INDEX"

# Get the ID of the next monitor
NEXT_MONITOR=$(echo "$MONITORS" | tr ' ' '\n' | head -n $((NEXT_INDEX + 1)) | tail -n 1)

# NEXT_MONITOR=$(echo "$MONITORS" | tr ' ' '\n' | sed -n "${NEXT_INDEX}p")

echo "Next Monitor: $NEXT_MONITOR"

# Move the current workspace to the next monitor
hyprctl dispatch movecurrentworkspacetomonitor "$NEXT_MONITOR"
