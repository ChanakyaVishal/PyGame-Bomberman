from Bomb import Bomb
from Enemy import Enemy
from Bricks import Bricks
from Bomberman import Bomberman
from Board import Board
import random as rd
from pynput.keyboard import Key, Listener
import time
import math as mt

# Coordinate System
# The coordinate system is such that each block of 4x2 is considered to be a coordinate
# The bottom left usable space is considered to be (0,0)
# Each entity would have a render block which would manipulate the game_array to display the output
# Max Coordinates (only I quadrant)= (21,21)


class essentials:
    board = Board()
    game_array = [[' ' for x in range(Board.width)] for y in range(Board.length)]
    bman = Bomberman(1, 1, 0, 3)
    bman.render()
    board.render_board()
    bombs = []
    enemies = []
    bricks=[]
    no_of_enemies=1
    no_of_bricks=10

    @staticmethod
    def mapping(x,y):
        temp=Board.coordinate_array[x][y]
        x=x*2
        y=y*4
        for i in range(x,x+2):
            for j in range(y,y+4):
                essentials.game_array[i][j] = temp

    @staticmethod
    def render_frame():
        for i in range(21):
            for j in range(21):
                essentials.mapping(i, j)
        essentials.output_frame()

    @staticmethod
    def output_frame():
        for i in range(Board.length):
            for j in range(Board.width):
                print(essentials.game_array[i][j],end='',flush=True)
            print("")

    @staticmethod
    def delete (x,y):
        Board.coordinate_array[x][y]=' '

    @staticmethod
    def Game_Start():
        essentials.render_elements()
        c=0
        while 1>0:
            essentials.render_frame()
            print('Score:{0} Lives:{1}'.format(essentials.bman.get_score(),essentials.bman.get_lives()))
            time.sleep(0.0000000000000000000001)
            essentials.listner()
            essentials.bomb_check()
            essentials.enemy_move()

            # Level 2 Initialisation
            if c==1:
                print("LEVEL 1 COMPLETED")
                for i in range(15):
                    print("\n")
                time.sleep(0.5)
                print("LEVEL 2")
                for i in range(15):
                    print("\n")
                time.sleep(1)

                essentials.no_of_enemies=5
                essentials.no_of_bricks=20
                x,y=essentials.bman.get_position()
                Board.coordinate_array[x][y]=' '
                essentials.render_elements()
                essentials.bman.set_position(1,1)
                essentials.bman.render()
                c=2

            # Level 3 Initialisation
            if c == 3:
                print("LEVEL 2 COMPLETED")
                for i in range(15):
                    print("\n")
                time.sleep(0.5)
                print("LEVEL 3")
                for i in range(15):
                    print("\n")
                time.sleep(1)

                essentials.no_of_enemies = 8
                essentials.no_of_bricks = 25
                x,y=essentials.bman.get_position()
                Board.coordinate_array[x][y] = ' '
                essentials.bman.set_position(1,1)
                essentials.render_elements()
                essentials.bman.render()
                c=4
            if essentials.enemies == []:
                c+=1

    @staticmethod
    def render_elements():
        for i in range(essentials.no_of_enemies):
            a,b = essentials.gen_random()
            enemy=Enemy(a,b)
            essentials.enemies.append(enemy)
        for i in range(essentials.no_of_bricks):
            a,b = essentials.gen_random()
            brick=Bricks(a,b)
            essentials.bricks.append(brick)

    @staticmethod
    def gen_random():
        temp1=rd.randint(5,18)
        temp2=rd.randint(5,18)
        if Board.coordinate_array[temp1][temp2]==' ':
            print(temp1)
            print(temp2)
            return temp1, temp2
        else:
            return essentials.gen_random()

    @staticmethod
    def move(direction):

        x, y = Bomberman.get_position(essentials.bman)
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
        if Board.coordinate_array[x+dx][y+dy] == Enemy.symbol:
            x, y = essentials.bman.get_position()
            essentials.bman.die()
            Board.coordinate_array[x][y] = ' '
            Board.coordinate_array[1][1] = Bomberman.symbol
            essentials.bman.set_position(1, 1)
        if Board.coordinate_array[x+dx][y+dy] == ' ' or (Board.coordinate_array[x+dx][y+dy] in range(0,4)):
            Board.coordinate_array[x][y]=' '
            essentials.bman.move(dx,dy)
        else:
            pass
    @staticmethod
    def on_press(key):
        try:
            if key.char == 'b':
                x, y = essentials.bman.get_position()
                bomb=Bomb(x,y,5)
                if essentials.bombs == []:
                    essentials.bombs.append(bomb)
            else:
                essentials.move(key.char)
        except:
            pass
        return False

    @staticmethod
    def listner():
        with Listener(on_press=essentials.on_press) as listener:
            listener.join()


    @staticmethod
    def bomb_check():
        for bomb in essentials.bombs:
            bomb.timer_red()
            if bomb.get_timer() == 0:
                essentials.check_surroundings_bman(bomb)
                essentials.check_surroundings_enemies(bomb)
                essentials.check_surroundings_brick(bomb)
                bomb.ready_detonate()
            if bomb.get_timer() == -1:
                bomb.detonate()
                essentials.bombs.remove(bomb)
    @staticmethod
    def enemy_move():
        for enemy in essentials.enemies:
            enemy.move()

    @staticmethod
    def check_surroundings_bman(bomb):
        a, b=essentials.bman.get_position()
        if (a - bomb.x in range(-1, 2) and b - bomb.y in range(-1, 2) )and (a - bomb.x ==0 or b - bomb.y ==0):
            x, y = essentials.bman.get_position()
            essentials.bman.die()
            Board.coordinate_array[x][y]=' '
            Board.coordinate_array[1][1]=Bomberman.symbol
            essentials.bman.set_position(1,1)


    @staticmethod
    def check_surroundings_enemies(bomb):
        for enemy in essentials.enemies:
            a, b = enemy.get_position()
            if (a - bomb.x in range(-1, 2) and b - bomb.y in range(-1, 2) )and (a - bomb.x ==0 or b - bomb.y ==0):
                enemy.die()
                essentials.enemies.remove(enemy)
                essentials.bman.inc_score(100)

    @staticmethod
    def check_surroundings_brick(bomb):
        for brick in essentials.bricks:
            a, b = brick.get_position()
            if (a - bomb.x in range(-1, 2) and b - bomb.y in range(-1, 2) )and (a - bomb.x ==0 or b - bomb.y ==0):
                brick.destroy()
                essentials.bricks.remove(brick)
                essentials.bman.inc_score(20)

if __name__=='__main__':
    essentials.Game_Start()