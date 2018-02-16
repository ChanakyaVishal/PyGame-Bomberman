from Entity import *


class Person(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y)

# move one step at a frame
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.render()