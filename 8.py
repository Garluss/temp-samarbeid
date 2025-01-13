print("Dette programmet treng hjelp!")

class Board():
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.board = {}
    
    def load(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.board[(x,y)] = "#"
    
    def draw(self):
        final_str = ""
        t = 0
        for i in self.board:
            #final_str = final_str + "\n"
            if t == self.size_x:
                final_str = final_str + "\n"
                t = 0
            for y in self.board[i]:
                final_str = final_str + " " + y + " "
                t += 1
        print(final_str)

board1 = Board(15,15)

board1.load()
board1.draw()