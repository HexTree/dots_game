class Game():

    board = [[0]]
    turn = 1

    def __init__(self, n):
        self.board = [[0]*n for _ in xrange(n)]
        self.turn = 1

    def end_turn(self):
        self.turn = 3 - self.turn

    def get_board(self):
        return self.board

    def put_counter(self, i, j):
        if self.board[i][j] != 0:
            return
        self.board[i][j] = self.turn
        self.end_turn()