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
play(files[0])
time.sleep(20)