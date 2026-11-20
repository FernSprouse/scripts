#!/usr/bin/env sh

# this script fixes a problem with xbox controllers on UNBEATABLE
# unfortunately, it means you are stuck with the default controller config
# forever because the fix involves deleting the Input-Bindings.json file
# in theory, one could just replace it with a properly configured file
# but I don't mind the defaults *shrug*

# remove the user input json file
BFILE="/mnt/games/SteamLibrary/steamapps/compatdata/2240620/pfx/drive_c/users/steamuser/AppData/LocalLow/D-CELL GAMES/UNBEATABLE/SYSTEM/Input-Bindings.json"
if [ -e "$BFILE" ]; then
    rm "$BFILE"
fi
