from Bomberman import Bomberman
from Enemy import Enemy
from Entity import Entity
from Board import Board,Wall

class Bomb(Entity):
    symbol='e'

    def __init__(self,x,y,timer):
        Entity.__init__(self,x,y)
        self.symbol='e'
        self.timer=timer


    def get_timer(self):
        return self.timer

    def timer_red(self):
        self.timer=self.timer-1
        if Board.coordinate_array[self.x][self.y] != Bomberman.symbol and Board.coordinate_array[self.x][self.y] != Enemy.symbol:
            Board.coordinate_array[self.x][self.y]=self.timer
    def ready_detonate(self):
        x=self.x
        y=self.y
        if Board.coordinate_array[x][y+1] != Wall.symbol:
            Board.coordinate_array[x][y+1] = self.symbol
        if Board.coordinate_array[x][y-1] != Wall.symbol:
            Board.coordinate_array[x][y-1] = self.symbol
        if Board.coordinate_array[x+1][y] != Wall.symbol:
            Board.coordinate_array[x+1][y]=self.symbol
        if Board.coordinate_array[x-1][y] != Wall.symbol:
            Board.coordinate_array[x-1][y] = self.symbol
        Board.coordinate_array[self.x][self.y] = self.timer
    def detonate(self):
        x=self.x
        y=self.y
        if Board.coordinate_array[x + 1][y] == self.symbol:
            Board.coordinate_array[x + 1][y] = ' '
        if Board.coordinate_array[x - 1][y] == self.symbol:
            Board.coordinate_array[x - 1][y] = ' '
        if Board.coordinate_array[x][y - 1] == self.symbol:
            Board.coordinate_array[x][y - 1] = ' '
        if Board.coordinate_array[x][y + 1] == self.symbol:
            Board.coordinate_array[x][y + 1] = ' '
        Board.coordinate_array[x][y] = ' '