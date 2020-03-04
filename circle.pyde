start = 0
iter = 0
col = 0

def setup():
    size(1000, 1000)
    frameRate(48)
    background(255,255,255)
    
t=0 
q=0  
k=0 
def draw():
    background(230,230,230)
    #t=0;
    global t, q, col,k;
    j = 0;
    straight = []
    cir = []
    

    modX = 100*(sin(q + (3 * PI)/2) + 1)

    #fill(0,0,0)
    stroke(0,0,0)
    for i in range(0,21):
        circle(300+i*20,500,3)
        straight.append([300+i*20,500])


    while j <= 20:  
        circle(500 + (modX+200)*cos(t), 500 + (modX+200)*sin(t), 3)
        cir.append([500 + (modX+200)*cos(t), 500 + (modX+200)*sin(t)])
        j+=1
        t = t + PI/10.5
        
    stroke(col, col, col,)    
    col = 100*(sin(q + (3 * PI)/2) + 1)  
    for b in range(0, 21):
        line(straight[b][0], straight[b][1], cir[b][0], cir[b][1]) 
        #print(straight[b][0], straight[b][1], cir[b][0], cir[b][1])
        print(straight[b][0])
    
        
    saveFrame("circle-######.png");
        
    if k == 1279:
        noLoop()    
    
    t = t + PI/160
        
    q = q + PI/320
    
    k = k+1
    
        
        


    
