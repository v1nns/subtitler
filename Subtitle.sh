IFS_BAK=$IFS
IFS="
"

for line in $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS; do
        full_path="/home/"$USER"/projects/subtitler/"subtitler.py
        #python $full_path $line 
	output="$(python3 "$full_path" "$line" 2>&1)"
       	echo "$output" #| tee out.txt	
done

notify-send "Script executed with success!"

IFS=$IFS_BAK




##to do::#give a check here to see if the files coming are .mp4........videoformat files only otherwise exit.....
#to do::also we can give languagae as second parameter
#path to save in ~/.gnome2/nautilus-scripts
