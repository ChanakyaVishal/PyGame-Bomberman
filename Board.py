from Wall import Wall

class Board:
    length = 42
    width = 84
    coordinate_array = [[' ' for p in range(21)] for q in range(21)]

    def __init__(self):
        pass

    def render_board(self):
        for i in range(Wall.blocks):
            Board.coordinate_array[0][i] = Wall.symbol
        for i in range(Wall.blocks):
            Board.coordinate_array[20][i] = Wall.symbol

        for i in range(Wall.blocks):
            Board.coordinate_array[i][0] = Wall.symbol
        for i in range(Wall.blocks):
            Board.coordinate_array[i][Wall.blocks - 1] = Wall.symbol
        for i in range(1, Wall.blocks):
            for j in range(1, Wall.blocks - 2):
                if i % 2 == 0 and j % 2 == 0:
                    Board.coordinate_array[i][j] = Wall.symbol
