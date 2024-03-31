#!/usr/bin/bash

#migueldeoleiros: Match 2024

#simple power menu 


rofi_cmd(){
    rofi \
    -theme-str 'window {width: 300px; height: 170;}' \
    -dmenu -i \
    -p "POWER MENU"
}

selection=`echo -e "Poweroff\nReboot\nExit Hyprland\n" | rofi_cmd`

case ${selection} in
    "Poweroff")
        poweroff
        ;;
    "Reboot")
        reboot
        ;;
    "Exit Hyprland")
        killall Hyprland
        ;;
esac

