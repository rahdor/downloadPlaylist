#!/bin/bash
sudo pip install -r requirements.txt
python downloadMp3.py 
mkdir mp3
mv *.mp3 mp3/