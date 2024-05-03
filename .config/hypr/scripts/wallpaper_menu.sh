#!/usr/bin/bash

#migueldeoleiros: April 2024

#wallpaper changer menu 

wallpaper_dir="$HOME/wallpapers"
wallpaper_script="$HOME/.config/hypr/wallpaper.sh"

rofi_cmd(){
    rofi \
    -theme-str 'window {width: 500; height: 500;}' \
    -dmenu -i \
    -p "SELECT WALLPAPER"
}

get_selection(){
    local dir_file="$1"

    if [[ -d $dir_file ]]; then
        selected=$(ls "$dir_file" | rofi_cmd)
        if [[ "$selected" == "" ]]; then
            echo "" #exit on ESC
        else
            get_selection "$dir_file/$selected"
        fi
    elif [[ -f $dir_file ]]; then
        echo "$dir_file"
    else
        echo ""
    fi
}

selection=$(get_selection "$wallpaper_dir")
echo "$selection"

if [[ -n $selection ]]; then
    swww img $selection --transition-type center
    echo "swww img $selection --transition-type center"
    echo "swww img $selection" > $wallpaper_script
    chmod +x "$wallpaper_script"
fi
