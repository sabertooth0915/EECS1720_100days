def setup():
    size(480, 120)

def draw():
    if  mousePressed:
        fill(255)
    else:
        fill(0,255,0)
    ellipse(mouseX, mouseY, 80, 80)
