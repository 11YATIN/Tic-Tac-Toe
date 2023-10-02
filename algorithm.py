class tic_tac_toe:
    def __init__(self):
        self.grid=[[0,0,0],[0,0,0],[0,0,0]]
    
    def print_grid(self):
        print("\n")
        for i in range(3):
            for j in range(3):
                print(self.grid[i][j],end=" ")
            print("\n")
    
    def move(self, player, val):
        row = int(val/3)
        col = int(val%3)
        if (player=='X'):
            self.grid[row][col]=1
        else:
            self.grid[row][col]=-1

    def check_win(self):
        tie=1
        for i in range(3):
            l2r = 0
            u2d = 0
            for j in range(3):
                if(self.grid[i][j]==0):
                    tie = 0; 
                l2r += self.grid[i][j]
                u2d += self.grid[j][i]
            if (l2r == 3):
                return 10
            elif (l2r == -3):
                return -10
            elif (u2d == 3):
                return 10
            elif (u2d == -3):
                return -10
            
        diag_1 = self.grid[0][0]+self.grid[1][1]+self.grid[2][2];
        diag_2 = self.grid[0][2]+self.grid[1][1]+self.grid[2][0];
        if (diag_1 == 3):
            return 10
        elif (diag_1 == -3):
            return -10
        elif (diag_2 == 3):
            return 10
        elif (diag_2 == -3):
            return -10
        return tie
    

