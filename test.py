import os
from time import sleep

streamer = 'INSERT STREAMER'
os.chdir(f'INSERT PATH')



for i in os.listdir():
        os.rename(i, f'{i.replace(" ", "")}')

sleep(1)
for i in os.listdir():
       os.system(f"ffmpeg -i {i} -i {i} -filter_complex '[0:v]scale=2276:1280,boxblur=4[bg];[1:v]scale=720:-1[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2[tmp];[tmp]crop=720:1280:(2276-720)/2:0[out]' -map [out] -map 0:a /Users/keno/Desktop/clips/{i}")
       print('done')
