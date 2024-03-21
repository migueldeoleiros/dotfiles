#!/usr/bin/bash

#migueldeoleiros: Match 2024

#simple script that launches dmenu for killing processes

program=$(ps -u $USER -o comm,pid | awk 'NR > 1' | rofi -dmenu -i -p "kill")
pid=$(echo "$program" | awk '{print $NF}')
kill $program
