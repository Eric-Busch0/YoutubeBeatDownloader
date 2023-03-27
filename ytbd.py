import os, sys
from pytube import YouTube
import aubio

class YTBD:

    def __init__(self, url='',filePath='') -> None:
        self.url = url
        self.filePath = filePath
    
    def download(self):
        
        if self.url == '':
            raise Exception('URL cannot be empty!')
        print(f'Downloading {self.url}')
        try:

            yt = YouTube(self.url)


            dest = yt.streams[0].title + '.mp3' 
            dest = dest.replace('\"', '')
            dest = dest.replace('.mp4','')
            dest = dest.replace('*', '')

            video = yt.streams.filter(only_audio=True).first()
        
            outfile = video.download()

            if not os.path.exists(dest):
                os.rename(outfile,dest)
                self.filePath = dest
            else:
                raise Exception('Cannot copy to that location, already exists!')

        except Exception as e:
            print(str(e))


    def analyze(self):

        if os.path.exists(self.filePath):
            raise Exception(f'File {self.filePath} does not exist!')


        pass