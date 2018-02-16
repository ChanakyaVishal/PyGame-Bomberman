from Person import Person
from Board import Board
import sys as sys

class Bomberman(Person):

    symbol = '\033[1;34m'+'B'+'\033[1;m'
    def __init__(self,x,y,score,lives):
        Person.__init__(self,x,y)
        self.score = score
        self.lives=lives

    def render(self):
        Board.coordinate_array[self.x][self.y] =Bomberman.symbol

    def inc_score(self,ds):
        self.score+=ds

    def get_score(self):
        return self.score

    def get_lives(self):
        return self.lives

    def set_position(self,x,y):
        self.x=x
        self.y=y

    def die(self):
        self.lives-=1
        if self.lives == 0:
            print("GAME OVER")
            sys.exit(0)
