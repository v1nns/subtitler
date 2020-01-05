Subtitler
=========

Python script to download subtitles of your movie/tv series episode using subliminal.

### Dependencies:
In order to execute it, you must install the following packages using pip:
* babelfish
* subliminal

### Usage:
If you have python in your path, simply drag and drop files and folders you wish to get subtitles from on subtitler.py

##### Windows:
* Place subtitler.py file to C:/

* Place the Subtitle.cmd in sendto folder in windows (can be accessed by typing shell:sendto in address bar and must change the PATH variable to python folder).

* Right click the movie file (not the movie folder). You can also select multiple files and click sendto -> Subtitle.cmd

##### Linux using Nautilus file manager:
* Install python

* Copy Subtitle.sh to ~/.local/share/nautilus/scripts/ (Ubuntu 13.04 or above) OR ~/.gnome2/nautilus-scripts/ (Ubuntu 12.10 and below) folder (note: must change the path pointing to python script).

* Execute the following command to make the script executable:
```
chmod +x ~/.local/share/nautilus/scripts/Subtitle.sh
```

* Now Right Click on the movie file (not the movie folder). You can also select multiple files. Click Scripts -> Subtitle.

That's all, folks! The .srt subtitle file will be created right next to your movie file and it will appear a message box saying the script executed with success.
