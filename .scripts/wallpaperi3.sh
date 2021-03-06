#!/usr/bin/env bash
#
#migueldeoleiros: September 2020
#
#This is a simple script to change the Wallpaper on my i3 config through a rofi menu
#It requires to restart i3 to see the changes
#
set -euo pipefail

NewWallName=$(ls ~/wallpapers | rofi -dmenu -i -p)
NewWall='~/wallpapers/'$NewWallName''
OldWall=$(grep 'exec_always feh' ~/.config/i3/config | awk '{print $4}')
sed -i 's#'$OldWall'#'$NewWall'#g' ~/.config/i3/config
