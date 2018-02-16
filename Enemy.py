from Person import Person
from Board import Board
import random as rd

class Enemy(Person):
    symbol ='\033[1;31m'+'E'+'\033[1;m'

    def __init__(self,x,y):
        Person.__init__(self, x, y)
        self.render()

    def render(self):
        Board.coordinate_array[self.x][self.y]=Enemy.symbol

    def move(self):
        temp=rd.random()
        if temp<=0.25:
            direction='w'
        elif temp>0.25 and temp<=0.5:
            direction='a'
        elif temp>0.5 and temp<=0.75:
            direction='s'
        elif temp > 0.75 and temp <= 1:
            direction = 'd'
        if direction == 'a':
            dx=0
            dy=-1
        elif direction == 'd':
            dx=0
            dy=1
        elif direction == 'w':
            dx=-1
            dy=0
        elif direction == 's':
            dx=1
            dy=0
        if (Board.coordinate_array[self.x+dx][self.y+dy]==' ' or (Board.coordinate_array[self.x+dx][self.y+dy] in range(0,4))) or Board.coordinate_array[self.x+dx][self.y+dy]=='B':
            Board.coordinate_array[self.x][self.y] = ' '
            self.x+=dx
            self.y+=dy
        self.render()

    def die(self):
        Board.coordinate_array[self.x][self.y] = ' '

