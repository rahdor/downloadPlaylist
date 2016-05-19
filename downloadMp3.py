import sys, pyperclip, youtube_dl
if len(sys.argv) > 1:
	url = ' '.join(sys.argv[1:])
else:
	url = pyperclip.paste()

options = {
    'format': 'bestaudio/best', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",      # convert to mp3 
    'outtmpl': "%(uploader)s-%(title)s.%(ext)s",        # name the file the ID of the video
    'noplaylist' : False,        # download playlists
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([url])




