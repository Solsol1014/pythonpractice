import os

while 1:
    videoaddress=input("video address:")

    if videoaddress=='exit':
        break

    videoname=input("video name:")
    ffmpegcommand='ffmpeg -headers "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36" -i "'+videoaddress+'" -c copy -bsf:a aac_adtstoasc "E:\\학교\\C프\\강의영상\\'+videoname+'.mp4"'

    os.system(ffmpegcommand)