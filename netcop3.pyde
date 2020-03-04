w = 5000
h = 5000
secondLater = []


def center(x, y, num_points, spread):
    ls = []
    for i in range(1, floor(num_points/2)+1):
        ls.append([x-(i*spread), y])
        ls.append([x+(i*spread), y])
    if num_points % 2 != 0:
        ls.append([x,y])
    return ls
    
    
def setup():
    size(5000,5000)
    frameRate(48)
    background(255,255,255)
    

def draw():   
    global h
    all_layers = []
    firstLayer = center(w/2, 0.075*h, 2, 125) 
    secondLayer = center(w/2, 0.4*h, 2, 125) 
    thirdLayer = center(w/2, 0.7*h, 1, 250) 
    fourthLayer = center(w/2, 0.9*h, 3, 625)
    fifthLayer = center(w/2, 0.95*h, 1, 500)
    #fifthLayer = center(w/2, 900, 5, 125)
    all_layers.append(firstLayer)
    all_layers.append(secondLayer)
    all_layers.append(thirdLayer)
    all_layers.append(fourthLayer)
    all_layers.append(fifthLayer)
    
    s = 250
    
    secondLayer.extend([[secondLayer[0][0] - s*1, secondLayer[0][1] - s*1], [secondLayer[0][0] - s*2, secondLayer[0][1] - s*2], [secondLayer[0][0] - s*3, secondLayer[0][1] - s*3]])
    
    secondLayer.extend([[secondLayer[1][0] + s*1, secondLayer[1][1] - s*1], [secondLayer[1][0] + s*2, secondLayer[1][1] - s*2], [secondLayer[1][0] + s*3, secondLayer[1][1] - s*3]])
    
    thirdLayer.extend([[thirdLayer[0][0] - s*1, thirdLayer[0][1] + s*1], [thirdLayer[0][0] + s*1, thirdLayer[0][1] + s*1]])
    
    strokeWeight(5)
    
    for i in range(len(all_layers)):
        for node in all_layers[i]:
            fill(0,0,0)
            circle(node[0], node[1], 15)
            if i < len(all_layers) - 1:
                for nextNodes in all_layers[i+1]:
                    line(node[0], node[1], nextNodes[0], nextNodes[1])
                    
    # for idx, ele in enumerate(fifthLayer):
    #     circle(ele[0], ele[1], 3)
    #     line(fifthLayer[idx][0], fifthLayer[idx][1], fourthLayer[idx][0], fourthLayer[idx][1])
     
    # fill(0,0,0)   
    # textAlign(CENTER);
    # for ele in thirdLayer:
    #     text("you", ele[0], ele[1]+50)
        
    saveFrame("circle-######.png");
                
    
    # for ele in firstLayer:
    #     circle(ele[0], ele[1], 3)
    #     for eleNext in secondLayer:
    #         line(ele[0], ele[1], eleNext[0], eleNext[1])
            
    # for ele in secondLayer:
    #     circle(ele[0], ele[1], 3)
    #     for eleNext in thirdLayer:
    #         line(ele[0], ele[1], eleNext[0], eleNext[1])
            
    # for ele in thirdLayer:
    #     circle(ele[0], ele[1], 3)
