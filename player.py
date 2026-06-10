import pygame
import time
from pathlib import Path
def scan_folder(folder_path):
    folder=Path(folder_path)
    files=list(folder.glob("*.mp3"))
    return files 
def play(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
class Player:
    def __init__(self,files):
        self.files=files
        self.index=0
        self.state="stopped"
    def play_current(self):
        file_path=self.files[self.index]
        play(file_path)
        self.state="playing"
        print(f"Now playing: {self.files[self.index].name}")
    def next(self):
        self.index+=1
        if self.index==len(self.files):
            self.index=0
        self.play_current()
    def pause(self):
        self.state="paused"
        pygame.mixer.music.pause()
    def resume(self):
        self.state="playing"
        pygame.mixer.music.unpause()
    def monitor(self):
        while True:
            if pygame.mixer.get_init() and pygame.mixer.music.get_busy()==False and self.state=="playing":
                self.next()
            time.sleep(1)
    def input_loop(self):
        while True:
            command=input("Enter a command:")
            if command=="pause":
                self.pause()
                print("paused")
            elif command=="resume":
                self.resume()
                print("resumed")
            elif command=="next":
                self.next()
                print(f"Playing: {self.files[self.index].name}")
            elif command=="quit":
                break
pygame.mixer.pre_init(44100,-16,2,2048)
pygame.mixer.init()
files=scan_folder("/home/yash/Desktop/musicplayer")
player=Player(files)
import threading
t=threading.Thread(target=player.monitor)
t.daemon=True
t.start()
player.play_current()
player.input_loop()
