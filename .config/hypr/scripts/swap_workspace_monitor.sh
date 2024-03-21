#!/usr/bin/env bash

CURRENT=$(hyprctl monitors -j | jq -r '.[] | select(.focused == true) | .id')

if [ "$CURRENT" = "0" ]; then
    MONITOR=1
else
    MONITOR=0
fi

hyprctl dispatch movecurrentworkspacetomonitor "$MONITOR"
