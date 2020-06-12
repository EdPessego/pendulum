'''
Author: Eduardo Barrancos
File: pendulum
Description: Manage the processing part
'''

from Cord_Bob import Pendulum

og = PVector(0,0)
leng = 15

p = None

def setup():
    global p
    
    size(640, 360)
    frameRate(30)
    
    og.x = width/2
    og.y = 0
    
    p = Pendulum(og, leng, 30)
    
def draw():
    global p
    
    background(255)
    
    p.go()
    
