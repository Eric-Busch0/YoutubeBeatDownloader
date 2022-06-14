# from infi.devicemanager import DeviceManager
# import usb.core
# import usb.util
# import libusb
import os
from pytube import YouTube
import re

ENDPOINT = 'https://www.youtube.com/watch?v=iywDcfW0bJ8'

def do_download(endpoint):
    try:

        yt = YouTube(endpoint)
        dest = yt.streams[0].title + '.mp3' 
        dest = dest.replace('\"', '')
        dest = dest.replace('.mp4','')
        dest = dest.replace('*', '')

        video = yt.streams.filter(only_audio=True).first()
        
        outfile = video.download()
        
        
        
        if not os.path.exists(dest):
            os.rename(outfile,dest)
        else:
            print('Cannot copy to that location, already exists!')
    except:
        print('An exception has occured')

    
def main():

    do_download(ENDPOINT)



if __name__ == "__main__":
    main()