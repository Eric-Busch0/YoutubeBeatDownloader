
import os, sys
from pytube import YouTube
# import rex
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-u','--url', action='extend', nargs='*', help='URL to download instrumental from')
parser.add_argument('-a','--analyze', action='extend', nargs='*')



args = parser.parse_args()

# print(args.url)

# ENDPOINT = 'https://www.youtube.com/watch?v=382mKYYNhY0&list=PL2ntw5yLXvVUoUlbNRb4dkL-EwTtycPFD&index=24' #your enpoint here

# def do_download(endpoint):
#     try:

#         yt = YouTube(endpoint)
#         dest = yt.streams[0].title + '.mp3' 
#         dest = dest.replace('\"', '')
#         dest = dest.replace('.mp4','')
#         dest = dest.replace('*', '')

#         video = yt.streams.filter(only_audio=True).first()
        
#         outfile = video.download()

#         if not os.path.exists(dest):
#             os.rename(outfile,dest)
#         else:
#             print('Cannot copy to that location, already exists!')
#     except Exception as e:
#         print(str(e))

    
def main():

   pass



if __name__ == "__main__":
    main()
