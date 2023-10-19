from random import randint

screenHeight = 500
screenWidth = 1000

boxes = []

class Box:
    def __init__(self, num, boxSize):
        self.num = num
        self.boxSize = boxSize
        self.pos = PVector(randint(100,screenWidth-100),randint(100,screenHeight-100))
        self.speed = PVector(randint(1,5), randint(1,5))
        
        #the length of the vector
        self.lineLength = self.pos.add(self.speed)
        
        rectMode(RADIUS)
        
    def show(self):
        #makes a rectangle
        fill('#FFFFFF')
        rect(self.pos.x, self.pos.y, self.boxSize, self.boxSize)
        fill('#F66C6C')
        
        #the end point of the line
        self.lineEndpoint = PVector(self.pos.x + self.speed.x * 10, self.pos.y + self.speed.y * 10)
        
        line(self.pos.x, self.pos.y, self.lineEndpoint.x, self.lineEndpoint.y)
    def update(self):
        #adds the speed to x and y position of recangle
        self.pos.add(self.speed)
        
        #bounces of the edge of the screen
        if (self.pos.x + self.boxSize) > screenWidth or (self.pos.x - self.boxSize) < 0:
            self.speed.x = self.speed.x * -1
        if (self.pos.y + self.boxSize) > screenHeight or (self.pos.y - self.boxSize) < 0:
            self.speed.y = self.speed.y * -1
        
    def collision(self):
        for obj in boxes:
            if obj != self:
                
                #calculates the distance between the two objs
                d = dist(self.pos.x, self.pos.y, obj.pos.x, obj.pos.y)
                
                if d < self.boxSize + obj.boxSize:
                    self.speed.mult(-1)
                    obj.speed.mult(-1)
            
    
def setup():
    size(screenWidth, screenHeight)
    for i in range(5):
        boxes.append(Box(i+1, randint(10,50)))

def draw():
    background('#192655')
    for obj in boxes:
        obj.show()
        obj.update()
        obj.collision()
