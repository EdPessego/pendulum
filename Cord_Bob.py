'''
Author: Eduardo Barrancos
File: pendulum
Description: Object for the pendulum
'''

'''
class cord:
    def __init__(self, origin, bob, ln):
        self.origin = origin
        self.bob = bob
        self.ln = ln
        
    def update_pos(self, angle):
        self.bob.x = self.origin.x + self.ln * sin(angle)
        self.bob.y = self.origin.y + self.ln * cos(angle)
        
    def draw_line(self):
        line(self.origin.x, self.origin.y, self.bob.x, self.bob.y)
        
class bob:
    def __init__(self, pos):
        self.pos = pos
    
    def update_pos(self, angle, rod):
        self.pos.x = rod.origin.x + rod.ln * sin(angle)
        self.pos.y = rod.origin.y + rod.ln * cos(angle)
        
    def draw_bob(self):
        ellipse(self.pos.x, self.pos.y, 32,32)
'''
    
class Pendulum:
    def __init__(self, origin, arm, radius):
        self.pivot = origin
        self.arm_s = arm * 10
        self.radius = radius
        
        self.GRAVITY = 9.8
        
        self.angle = PI/4
        self.vel = 0
        self.acc = -1 * (self.GRAVITY/self.arm_s) * sin(self.angle)
        
        self.pos = PVector(0,0)
        
    def update(self):
        self.pos.x = self.pivot.x + self.arm_s * sin(self.angle)
        self.pos.y = self.pivot.y + self.arm_s * cos(self.angle)
        
        self. acc = -1 * (self.GRAVITY/self.arm_s) * sin(self.angle)
        self.vel += self.acc
        self.angle += self.vel
        
        self.vel *= 0.99
        
    def draw_pendulum(self):
        line(self.pivot.x, self.pivot.y, self.pos.x, self.pos.y)
        ellipse(self.pos.x, self.pos.y, self.radius, self.radius)
        
    def go(self):
        self.update()
        self.draw_pendulum()
        
        
        
        
