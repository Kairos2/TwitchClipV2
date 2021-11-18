from __future__ import unicode_literals
import youtube_dl

ydl_opts = {'key': 'mp4'}

def twitch_dl(link):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
