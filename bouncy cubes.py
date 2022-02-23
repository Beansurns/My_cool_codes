#bouncy squares

import pygame




pygame.init()
s_width,s_height = 1200,800
screen = pygame.display.set_mode([s_width,s_height])
ignore_me = 1

fps = 90
clock = pygame.time.Clock()

mass_1 = 1
#ADJUST MASS OF SECOND WEIGHT HERE
mass_2 = 100

#you can adjust the colours of the squares here
colour_1 = (245,211,0)
colour_2 = (254,83,187)

#you can adjust font colour here
font_colour = (255,255,255)

collisions = 0

class Squares:
    def __init__(self,width=100,height=100,pos=(1180,780),vel=(0,0), mass = 100,colour=(245,211,0)):
        self.width = width
        self.height = height
        self.pos = pos
        self.vel = vel
        self.colour = colour
        self.new = False
        self.mass = mass
        self.font = pygame.font.SysFont('Comic Sans', 40)
        
    def update(self):
        global ignore_me
        ignore_me += 1 
        self.pos = (self.pos[0] + self.vel[0],self.pos[1])
        
        if self.vel == 0:
            self.new = True
        
        if self.pos[0] <= 0 and not self.new:
            self.vel = (self.vel[0] * -1,0)
            
        
        if ignore_me == 100:
            squares.append(Squares(200,200,(650,600),(-0.3,0),mass_2,colour_2))
            
        
             
        
        self.draw()
    
    
    def draw(self):
        pygame.draw.rect(screen,self.colour,(self.pos[0],self.pos[1],self.width,self.height))
        
        
        
        
b = 0       

square_num = 1
squares = [Squares(100,100,(400,700),(-0,0),mass_1,colour_1) for i in range(square_num)]
running = True
while running:
    b += 1
    
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if squares[0].pos[0] <= 0 and not squares[0].new:
        collisions += 1
        print(collisions)
                
                
    if b % 2 == 0:        
        for i in range(1,len(squares)):
            
            
                
            if abs(squares[0].pos[0] - squares[i].pos[0]) <= (squares[0].width + 1) and not squares[0].new:
                
                collisions += 1
                print(collisions)
                
                vel_1 = squares[i].vel[0]
                vel_2 = squares[0].vel[0]
        
                squares[0].vel = ((((2*mass_2)/(mass_2 + mass_1))*vel_1) + ((mass_1 - mass_2)/(mass_1 + mass_2)*vel_2),0)
                squares[i].vel = ((((2*mass_1)/(mass_2 + mass_1))*vel_2) + ((mass_2 - mass_1)/(mass_1 + mass_2)*vel_1),0)
                
    clock.tick(900)
    
            
    screen.fill((43,45,47))
    for square in squares:
        square.update()
        
        screen.blit(squares[0].font.render("collisions:  "+str(collisions), True, (255,255,255)), (800, 100))
        screen.blit(squares[0].font.render(str(mass_1), True, font_colour), (squares[0].pos[0] + squares[0].width/2.5, squares[0].pos[1] + squares[0].height/4))
        if b >= 100:
            screen.blit(squares[1].font.render(str(mass_2), True, font_colour), (squares[1].pos[0] + squares[1].width/4.6, squares[1].pos[1] + squares[1].height/2.7))
    pygame.display.flip()
            
pygame.quit()
        
        