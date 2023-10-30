import os
import time
import random
class Music:
    def __init__(self) -> None:
        self.song_list = {"dalimjanov" : "Hat Trick",
                          "Justin Timberlake" : "Cry Me a River",
                          "Konsta" : "Maska",
                          "Tom Odell" : "Another Love"}

class Player(Music):
    def __init__(self) -> None:
        super().__init__()
    def play(self):
        print(self.song_list)
        self.time = 0
        self.time += 1
        s=0
        m=0
        i = 0
        while s<=60:
            self.fav = []
            os.system('cls')
            print(f"Now playing: \n{list(self.song_list.values())[i]} - {list(self.song_list.keys())[i]}")
            self.a = list(self.song_list.keys())[i]
            print (f"\n{m} Minutes {s} Seconds\n\n\n\nYour favourite music(s): {self.fav}")
            time.sleep(1)
            s+=1
            if s==60:
                m+=1
                s=0
                if m == 1:
                    self.favtemp = int(input("Do you want to add this song to your favourites?\n1)Yes\n2)No\n"))
                    if self.favtemp == 1:
                        self.fav.append(a)
                    else:
                        pass
                    m = 0
                    s = 0
                    i += 1
                    if i == len(self.song_list.values()):
                        i = 0
        
music = Music()
player = Player()
a = input("To play music, type \"play\"\n")
if a.lower() == "play":
    player.play()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
song_list = {"dalimjanov" : "Hat Trick",
            "Justin Timberlake" : "Cry Me a River",
            "Konsta" : "Maska"}
x = song_list.items()
print(x)
