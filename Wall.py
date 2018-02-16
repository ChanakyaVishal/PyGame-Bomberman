class Wall:
    # Here blocks denote the total number of wall blocks[2x4] that exist on the board
    # block*2 = Max length
    # blocks*4 = Max width

    blocks = 21
    symbol = 'X'
    def __init__(self,blocks):
        self.blocks=blocks

