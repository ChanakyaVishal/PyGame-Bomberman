from Entity import Entity
from Board import Board
class Bricks(Entity):
    length = 2
    width = 4
    symbol = '\033[1;30m'+'/'+'\033[1;m'

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.render()

    def render(self):
        Board.coordinate_array[self.x][self.y] = Bricks.symbol

    def destroy(self):
        Board.coordinate_array[self.x][self.y] = ' '
