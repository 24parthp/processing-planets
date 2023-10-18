from random import randint

screenHeight = 500
screenWidth = 1000

boxes = []

class Box:
    def __init__(self, num, boxSize):
        self.num = num
        self.boxSize = boxSize
        self.pos = PVector(randint(100,screenWidth-100),randint(100,screenHeight-100))
        self.speed = PVector(randint(1,10), randint(1,10))
        
        #the length of the vector
        self.lineLength = self.pos.add(self.speed)
        
    def show(self):
        #makes a rectangle
        fill('#FFFFFF')
        rect(self.pos.x, self.pos.y, self.boxSize, self.boxSize)
        fill('#F66C6C')
        line(self.pos.x +  self.boxSize/2, self.pos.y +  self.boxSize/2, self.lineLength.x*1.1, self.lineLength.y*1.1)
    def update(self):
        #adds the speed to x and y position of recangle
        self.pos.add(self.speed)
        
        #bounces of the edge of the screen
        if (self.pos.x + self.boxSize) > screenWidth or (self.pos.x) < 0:
            self.speed.x = self.speed.x * -1
        if (self.pos.y + self.boxSize) > screenHeight or (self.pos.y) < 0:
            self.speed.y = self.speed.y * -1
    
def setup():
    size(screenWidth, screenHeight)
    for i in range(5):
        boxes.append(Box(i+1, randint(10,50)))

def draw():
    background('#192655')
    for obj in boxes:
        obj.show()
        obj.update()
