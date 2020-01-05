#!/usr/bin/env python3
import os
import logging
import sys
from babelfish import *
from subliminal import *
from datetime import timedelta

def sub_downloader(file_path):
    # open video from file path
    video = Video.fromname(file_path)
    
    # download
    #best_subtitle = download_best_subtitles([video], {Language('eng')}, providers=['opensubtitles'])
    best_subtitle = download_best_subtitles([video], {Language('por', 'BR')}, providers=['opensubtitles'])
    
    # save it to disk, next to the video
    save_subtitles(video, best_subtitle[video])
    
def main():
    root, _ = os.path.splitext(sys.argv[0])
    logging.basicConfig(filename=root + '.log', level=logging.INFO)
    logging.info("Started with params " + str(sys.argv))

    if len(sys.argv) == 1:
        print("This program requires at least one parameter")
        sys.exit(1)
    
    path = sys.argv[1]
    print("Searching subtitle for video: " + os.path.basename(path))
    sub_downloader(path)

if __name__ == '__main__':
    main()
