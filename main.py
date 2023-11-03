from pytube import YouTube
import os
import time
import sys


l = ' <~> '

def print_slow(_str):
    for letter in _str:
        sys.stdout.write(letter);sys.stdout.flush();time.sleep(0.04)


def main():
    def downloader(url):
        youtubeObject = YouTube(url)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download()
        except:
            print(f"\n{l}An error has occurred! Please check the video url to be a valid one.")
        print(f"\n{l}Video downloaded successfully!")
        time.sleep(1.5)
        #print_slow("\nThank you for using tool!")
        input(f"\n{l}Press enter to quit: ")
    os.system('cls')
    os.system('color D')
    print("""

_____.___.              __       ___.            ________                      .__                    .___            
\__  |   | ____  __ ___/  |_ __ _\_ |__   ____   \______ \   ______  _  ______ |  |   _________     __| _/___________ 
 /   |   |/  _ \|  |  \   __\  |  \ __ \_/ __ \   |    |  \ /  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ \\
 \____   (  <_> )  |  /|  | |  |  / \_\ \  ___/   |    `   (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/
 / ______|\____/|____/ |__| |____/|___  /\___  > /_______  /\____/ \/\_/|___|  /____/\____(____  /\____ |\___  >__|   
 \/                                   \/     \/          \/                  \/                \/      \/    \/        
                                                                                                               v1

""")
    url = input(f"\n\n{l}Enter a video url: ")
    time.sleep(1.5)
    print(f"\n{l}Downloading the video, please wait...")
    downloader(url)
    

if __name__ == '__main__':
    main()
