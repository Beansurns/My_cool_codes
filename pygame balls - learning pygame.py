import pygame
from random import randint as rand
import colorsys

pygame.init()
width,height = 1900,950
screen = pygame.display.set_mode([width,height])
G = 0.00981
limit = 10

class Ball:
    def __init__(self,radius=20,pos=(600,100),vel=(0.01,0),colour=(255,255,255)):
        self.radius = radius
        self.colour = colour
        self.pos = pos
        self.vel = vel
        self.new = True
    
    def update(self):
        self.vel = (self.vel[0],self.vel[1]+G)
        self.pos = (self.pos[0]+self.vel[0],self.pos[1]+self.vel[1])
        if self.pos[1] + self.radius >= height and not self.new:
            self.vel = (self.vel[0],self.vel[1] * -1)
            rep = rand(0,1)
            big = rand(0,100)
            if rep == 1 and len(balls) < limit:
                self.radius *= rand(85,100)/100
                balls.append(Ball(self.radius,self.pos,(-self.vel[0]+(rand(-30,30)/1000),self.vel[1]+(rand(-30,30)/1000))))
            #if big == 1 and len(balls) < limit:
                #balls.append(Ball(50,self.pos,(-self.vel[0]+(rand(-30,30)/1000),self.vel[1]+(rand(-30,30)/1000))))
                
        if self.pos[0] + self.radius >= width or self.pos[0] - self.radius <= 0:
            self.vel = (self.vel[0] * -1,self.vel[1])
            
        
               
               
        r,g,b = colorsys.hsv_to_rgb((self.pos[0]/width), 1, 1) 
        self.colour = (r*255,g*255,b*255)
        if round(self.vel[1]) == 0:
            self.new = False
        self.draw()
    
    
    def draw(self):
        pygame.draw.circle(screen,self.colour,self.pos,self.radius)
    
    
    
ball_num = 1
balls = [Ball(rand(20,50),(rand(200,700),rand(200,500)),(rand(5,20)/10*(rand(0,1)*2-1),0)) for i in range(ball_num)]
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    for i in range(len(balls)-1):
        for j in range(i+1,len(balls)):
            if (balls[i].pos[0] - balls[j].pos[0])**2 + (balls[i].pos[1] - balls[j].pos[1])**2 <= (balls[i].radius + balls[j].radius)**2 and not balls[i].new and not balls[j].new:
                
                balls[i].vel = (balls[i].vel[0] * -1,balls[i].vel[1])
                balls[j].vel = (balls[j].vel[0] * -1,balls[j].vel[1])
            
            
    screen.fill((0,0,0))
    for ball in balls:
        ball.update()
    pygame.display.flip()
            
pygame.quit()