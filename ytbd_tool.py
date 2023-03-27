
import os, sys
from pytube import YouTube
# import rex
import argparse
from ytbd import YTBD

parser = argparse.ArgumentParser()
parser.add_argument('-u','--url', action='extend', nargs='+', help='URL to download instrumental from')
parser.add_argument('-f','--file', action='extend', nargs='+', help='file path to instrumental')
parser.add_argument('-a','--analyze', default=False,action='store_true', help='print analysis results')
parser.add_argument('-o','--output', default='', help='name to save download as')
parser.add_argument('-ao', '--auto-output',default=False,action='store_true')
args = parser.parse_args()

print(args)


ENDPOINT = 'https://www.youtube.com/watch?v=382mKYYNhY0&list=PL2ntw5yLXvVUoUlbNRb4dkL-EwTtycPFD&index=24' #your enpoint here


    
def main():

   beat = YTBD(url=ENDPOINT,filePath=args.file)

   beat.download()



   pass



if __name__ == "__main__":
    main()
