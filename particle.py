import random
from time import sleep 
import pygame as pg

class Particle():
    def __init__(self, maxx, maxy):
        self.x = random.randint(0, maxx)
        self.y = random.randint(0, maxy)
        self.r = random.randint(1, 30)
        self.red = random.randint(1,255)
        self.green = random.randint(1,255)
        self.blue = random.randint(1,255)
        print(self.x, self.y)
    
    def draw(self,s):
        self.r += 0.01
        if(self.r > 50):
            self.r = 20
        self.x += 1
        if(self.r < 50):
            self.x = random.randint(0, 600)
        pg.draw.circle(s, (self.red,self.green,self.blue), (self.x,self.y), self.r)
