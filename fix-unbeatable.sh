#!/usr/bin/env sh

# remove the user input json file
BFILE="/mnt/games/SteamLibrary/steamapps/compatdata/2240620/pfx/drive_c/users/steamuser/AppData/LocalLow/D-CELL GAMES/UNBEATABLE/SYSTEM/Input-Bindings.json"
if [ -e "$BFILE" ]; then
    rm "$BFILE"
fi
