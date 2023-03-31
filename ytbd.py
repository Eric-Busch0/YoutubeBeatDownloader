import os, sys
from pytube import YouTube
import aubio
import keyfinder
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
            self.filePath = dest
            if not os.path.exists(dest):
                os.rename(outfile,dest)
                self.filePath = dest
            else:
                raise Exception('Cannot copy to that location, already exists!')

        except Exception as e:
            print(str(e))
    
    def getKey(self):
        if not os.path.exists(self.filePath):
            raise Exception(f'File {self.filePath} does not exist!')
        
        return keyfinder.key(self.filePath)
        
    def getTempo(self):
        return 120
    

    def autoRename(self,baseName):
        
        key = self.getKey()
        tempo=self.getTempo()

        newPath = f'{baseName}_{key}_{tempo}bpm.mp3'

        if os.path.exists(self.filePath):
            os.rename(self.filePath, newPath)
            self.filePath = newPath
        
    def analyze(self):
      
        key = self.getKey()
        tempo = self.getTempo()

        return {'key' : key, 'tempo' : tempo}
        pass