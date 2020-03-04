back = 255
balls = []
all_links = []
checked = []

class cir(object):
    
    def __init__(self, xpos, ypos, noise_val, stroke_color, radius, tx, ty, number, collided, checked, spread_index):
        self.xpos = xpos
        self.ypos = ypos
        self.noise_val = noise_val
        self.stroke_color = stroke_color
        self.radius = radius
        self.tx = tx
        self.ty = ty
        self.number = number
        self.collided = collided
        self.links = []
        self.checked = checked
        self.spread_index = spread_index

        
    def move(self):
        noiseSeed(self.noise_val)
        dx = noise(self.tx + self.number)
        noiseSeed(self.noise_val + 50)
        dy = noise(self.ty + self.number)
        self.xpos = map(dx,0,1,0,1080)
        self.ypos = map(dy,0,1,0,1080)
        self.tx += 0.001
        self.ty += 0.001
        
            
    def collide(self):
        global balls, checked
        for iter in balls:
            if self.collided == True or iter.collided == True:
                if iter.checked == False and iter!= self:
                    delta_x = iter.xpos - self.xpos
                    delta_y = iter.ypos - self.ypos
                    distance = sqrt(delta_x * delta_x + delta_y * delta_y)
                    if distance <= self.radius:
                        if self.collided == False and len(iter.links) <= 0:
                            self.spread_index = iter.spread_index + 1
                            iter.links.append(self)
                            
                            self.collided = True
                            iter.collided = True                        
                            self.stroke_color = (255,0,0)
                            iter.stroke_color = (255,0,0)   
                            
                        if iter.collided == False and len(self.links) <= 0:
                            iter.spread_index = self.spread_index + 1   
                            self.links.append(iter)   
                                          
                            self.collided = True
                            iter.collided = True                        
                            self.stroke_color = (255,0,0)
                            iter.stroke_color = (255,0,0)            
        self.checked = True    
                        
    def display_circles(self):
        fill(255)
        stroke(self.stroke_color[0], self.stroke_color[1], self.stroke_color[2])
        circle(self.xpos, self.ypos, self.radius)
        fill(0,0,0)
        #text(str(self.spread_index),self.xpos, self.ypos)
        text(str(len(self.links)),self.xpos, self.ypos)

                
    def display_lines(self):
        global all_links        
        for conn in self.links :
            d = sqrt((self.xpos - conn.xpos)**2 + (self.ypos - conn.ypos)**2)
            stroke(self.stroke_color[0], self.stroke_color[1] + d*0.25, self.stroke_color[2] + d*0.25)
            line(self.xpos, self.ypos, conn.xpos, conn.ypos)
            all_links.append((self,conn))
                
    def reset(self):
        self.checked = False

    
                
            
        
def setup():
    size(1080,1080)
    frameRate(60)
    background(back,back,back)
    balls.append(cir(random(0,1080), random(0,1080), int(random(0,50)), (255,0,0), 25, 0, 0, 0, True, False, 0))
    for i in range(1,31):
        balls.append(cir(random(0,1080), random(0,1080), int(random(0,50)), (0,0,0), 25, 0, 0, i, False, False, 999))
    
    
    
def draw():
    background(back,back,back)
    global all_links
    all_links = []


        
    for ele in balls:
            
        ele.move()
        
        ele.collide()
    
    for ele in balls:
        
        ele.display_lines()
        
    for ele in balls:
        
        ele.display_circles()
        
    for ele in balls:
        
        ele.reset()
        
        
        
        
        
