import pygame
import time
from pathlib import Path
def scan_folder(folder_path):
    folder=Path(folder_path)
    files=list(folder.glob("*.mp3"))
    return files 
def play(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
files=scan_folder("/home/yash/Desktop/musicplayer")
class Player:
    def __init__(self,files):
        self.files=files
        self.index=0
        self.state="stopped"
    def play_current(self):
        file_path=self.files[self.index]
        play(file_path)
        self.state="playing"
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
play(files[0])
time.sleep(20)