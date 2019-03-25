def setup():
    size(400,400)
    textSize(120)
    background(15,0,233)
def draw():
    if mousePressed:
        text("M", width/2-150, height/2)
        text("W", width/2+50, height/2)
        fill(175,150,150)       #staly
    if keyPressed == True:
        if key == 'm' or key == 'M':
            fill(110,0,25)      
        else:
            fill(175,150,150)   
        text("M", width/2-150, height/2)    
        if key == 'w' or key == 'W':
            fill(255, 51, 153)      
        else:
            fill(175,150,150)   
        text("W", width/2+50, height/2)    
        if keyCode == LEFT:
            fill(102, 255, 102)
            text("M", width/2-150, height/2)
        if keyCode == RIGHT:
            fill(255, 153, 0)
            text("W", width/2+50, height/2)    
    #print(mouseX,mouseY)   
    #print(hex(get(width/2-150, height/2)))
    s = createShape()
    s.beginShape()
    s.fill(0,100,100)
    s.stroke(17,0,111)
    s.vertex(80, height/3-200)
    s.vertex(width/2-50, height/3*2)
    s.vertex(width/2-30, height/2-100)
    s.vertex(width/2+60, height/2-500)
    s.endShape(CLOSE)
    shape(s, 50, 50)
