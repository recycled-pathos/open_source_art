points = []
p = 200
t=0
widths = []
w=280
ind = 0
rnd = 0
j=0
cir = [[510,100],[570,100],[510,980],[570,980]]

def gen_params():
    global t
    global p
    while t<2*PI:        
        p = 200 + 125*(sin(t) + 0.25)
        points.append([540-p, 540-p, p*2])
        t = t+PI/180

def setup():
    size(1080, 1080)
    frameRate(60)
    background(255,255,255)
    
gen_params()

def draw(): 
    background(255,255,255)   
    global p
    global w
    global t
    global ind
    global rnd

    j=0
    strokeWeight(1)
    noFill()
   

    # if rnd == 0:
    #     for y in range(1,ind):
    #         if y < 11:
    #             j=j+20
    #             stroke(j,j,j)
    #             line(cir[0][0],cir[0][1],points[ind-10*y][0],points[ind-10*y][1])
    #             line(cir[1][0],cir[1][1],points[ind-10*y][0]+points[ind-10*y][2], points[ind-10*y][1])             
    #             line(cir[2][0],cir[2][1],points[ind-10*y][0],points[ind-10*y][1]+points[ind-10*y][2])
    #             line(cir[3][0],cir[3][1],points[ind-10*y][0]+points[ind-10*y][2],points[ind-10*y][1]+points[ind-10*y][2])
    #             square(points[ind-10*y][0],points[ind-10*y][1],points[ind-10*y][2])
    #             circle(points[ind-10*y][0],points[ind-10*y][1],2)
    #             circle(points[ind-10*y][0]+points[ind-10*y][2], points[ind-10*y][1],2)
    #             circle(points[ind-10*y][0],points[ind-10*y][1]+points[ind-10*y][2],2)
    #             circle(points[ind-10*y][0]+points[ind-10*y][2],points[ind-10*y][1]+points[ind-10*y][2],2)


                
       

    for y in range(1,11):
        j=j+20
        stroke(j,j,j)
        line(cir[0][0],cir[0][1],points[ind-10*y][0],points[ind-10*y][1])
        line(cir[1][0],cir[1][1],points[ind-10*y][0]+points[ind-10*y][2], points[ind-10*y][1])         
        line(cir[2][0],cir[2][1],points[ind-10*y][0],points[ind-10*y][1]+points[ind-10*y][2])
        line(cir[3][0],cir[3][1],points[ind-10*y][0]+points[ind-10*y][2],points[ind-10*y][1]+points[ind-10*y][2])
        square(points[ind-10*y][0],points[ind-10*y][1],points[ind-10*y][2])        
        circle(points[ind-10*y][0],points[ind-10*y][1],2)
        circle(points[ind-10*y][0]+points[ind-10*y][2],points[ind-10*y][1],2)
        circle(points[ind-10*y][0],points[ind-10*y][1]+points[ind-10*y][2],2)
        circle(points[ind-10*y][0]+points[ind-10*y][2],points[ind-10*y][1]+points[ind-10*y][2],2)

    stroke(0,0,0)
    
    line(cir[0][0],cir[0][1],points[ind][0],points[ind][1])
    line(cir[1][0],cir[1][1],points[ind][0]+points[ind][2], points[ind][1])    
    line(cir[2][0],cir[2][1],points[ind][0],points[ind][1]+points[ind][2])
    line(cir[3][0],cir[3][1],points[ind][0]+points[ind][2],points[ind][1]+points[ind][2])
    circle(cir[0][0],cir[0][1], 10)
    circle(cir[1][0],cir[1][1], 10)
    circle(cir[2][0],cir[2][1], 10)
    circle(cir[3][0],cir[3][1], 10)
    
    strokeWeight(4)
    
    square(points[ind][0],points[ind][1],points[ind][2])
  
    if rnd <  4:
        saveFrame("line-######.png");
    if ind < len(points)-1:
        ind = ind+1    
    else:
        ind = 0
        rnd += 1
    
    
        

    
    
    
    
    
