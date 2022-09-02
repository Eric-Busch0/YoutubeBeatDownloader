
import os, sys
from pytube import YouTube
import re

ENDPOINT = 'https://www.youtube.com/watch?v=382mKYYNhY0&list=PL2ntw5yLXvVUoUlbNRb4dkL-EwTtycPFD&index=24' #your enpoint here

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
    except Exception as e:
        print(str(e))

    
def main(argv):

    print(argv)
    # do_download(ENDPOINT)
    for enpoint in argv:
        do_download(enpoint)



if __name__ == "__main__":
    main(sys.argv[1:])
