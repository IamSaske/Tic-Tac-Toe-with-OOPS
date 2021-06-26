"""
Step 1 - Take input
step2- Check validity of input
step3-check range of input
step4-find coordinates from input
step5- Check for empty position
step6- add to board
step7- Switch Users
step8- check for win condition
"""
class Board:
    def print_board(self,board):
        for row in board:
            for slots in row:
                print(f'{slots}',end=" ")
            print()
        pass

class User(Board):
    def quit(self,user_input):
        if user_input=='q':
            print('Thanks for playing')
            return True
        else:
            return False
    def check(self,user_input):
        if not user_input.isnumeric():
            print("Only numbers are allowed")
            return True
        return False

    def bounds(self,user_input):
        if int(user_input)<1 or int(user_input)>9:
            print('Input out of range')
            return True
        else :
         return False



class Board_coords(User):
    def coordinates(self,user_input):
        row=int(user_input/3)
        col=user_input
        if col>2: col=int(col%3)
        return (row,col)

    def istaken(self,coords,board):
        row=coords[0]
        col=coords[1]
        if board[row][col]!="-":
            print('position is already taken')
            return True
        return False

    def current_user(self, user):
        if user:
            return 'X'
        else:
            return 'O'

    def add_to_board(self, active_user,board,coords):
        row = coords[0]
        col = coords[1]
        board[row][col] = active_user



class Win(Board_coords):
    def isWin(self,board,active_user):
        if self.check_row(active_user,board): return True
        if self.check_col(active_user,board):return True
        if self.check_dig(active_user,board):return True

    def check_row(self,active_user,board):
        for row in board:
            row_completed=True
            for slot in row:
                if slot!=active_user:
                    row_completed=False
                    break
            if row_completed:return True
        return False

    def check_col(self,active_user,board):
        for col in range(3):
            col_completed=True
            for row in range (3):
                if board[row][col]!=active_user:
                    col_completed=False
                    break
            if col_completed: return True
        return False


    def check_dig(self,active_user,board):
        if (board[0][0]==active_user and board[1][1]==active_user and board[2][2]==active_user):return True
        if (board[0][2]==active_user and board[1][1]==active_user and board[2][0]==active_user):return True
        return False






if __name__ == '__main__':
    board=[["-","-","-"],#i=0
           ["-","-","-"],
           ["-","-","-"]]
    turns=0
    user=True
    player=Win()
    while turns<9:
        turns+=0
        active_user=player.current_user(user)
        player.print_board(board)
        user_input=input('Choose position between 1 to 9 or q to quit')
        if player.quit(user_input): break
        if player.check(user_input):
            print('try again')
            continue
        if player.bounds(user_input):
            print('try again')
            continue
        user_input=int(user_input)-1
        coords=player.coordinates(user_input)
        if player.istaken(coords,board):
         continue
        player.add_to_board( active_user,board,coords)
        if player.isWin(board,active_user):
            print(f'{active_user} WINS!!!')
            break



        if turns==9:print('Tie')
        user=not user







