import os

os.system('ffmpeg -headers "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36" -i "https://lmsvod.konkuk.ac.kr:1936/vod/mp4:wowza_vod/22940/405693/900761_720p.mp4/playlist.m3u8" -c copy -bsf:a aac_adtstoasc "E:\학교\C프\강의영상\C-3-1.mp4"')