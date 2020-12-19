# Connect 4 - ISU
# Gurkarn Dhaliwal
# November 29, 2019

from random import randint

row1 = [0, 0, 0, 0, 0, 0, 0]
row2 = [0, 0, 0, 0, 0, 0, 0]
row3 = [0, 0, 0, 0, 0, 0, 0]
row4 = [0, 0, 0, 0, 0, 0, 0]
row5 = [0, 0, 0, 0, 0, 0, 0]
row6 = [0, 0, 0, 0, 0, 0, 0]
    
column_numbers = '   1  2  3  4  5  6  7'
board = [row1, row2, row3, row4, row5, row6]

playerturns = 1
computerturns = 1

tips = ["If you see your opponent getting close to 4 in a row make sure you block them.", "Don't forget around the board to understand whats going on.", "Don't forget you can also win diagonally.", "Don't get caught up looking to win. Blocking is also an important part of the game"]

#Displays the current board
def printboard():
    row_numbers = 1
    print("\n-------CONNECT 4-------\n")
    print(column_numbers)
    for row in board:
        print(str(row_numbers)+"  "+str(row[0])+"  "+str(row[1])+"  "+str(row[2])+"  "+str(row[3])+"  "+str(row[4])+"  "+str(row[5])+"  "+str(row[6]))
        row_numbers += 1

def boardreset():
    for row in range(0,6):
        for i in range(0,7):
            board[row][i] = 0
            
#Places the piece and moves it to the lowest row that is avaliable in that column.
def placer(placement, token):
    for row in range(0,6):
        if board[row][placement] == 0:
            board[row][placement] = token
            if row != 0:
                oldrow = board[row-1]
                oldrow[placement] = 0
                
# Asks the player to choose a column to place a piece in
def player_placer(placement):
    global playerturns
    #Checks to make sure the column the user entered is one of the column and that the column that was chosen has space left in it
    if placement not in range(0,7):
        print("Invalid Column, Try Again")
        placement = int(input("Which Column Would You Like To Place A Piece: "))-1  
   
    while board[0][placement] != 0:
        print("\nThis Column is Full. Try Again")
        try:
            placement = int(input("Which Column Would You Like To Place A Piece: "))-1
        except:
            print("Numbers Only")
            
    placer(placement, 1)
    print("\nPlayer Turn "+str(playerturns)+"\nYou Placed The Piece In Column "+ str(placement + 1)+".")
    playerturns += 1

#Determines Next Move. Blocks if token = 1 and trys to win if token = 2.
def ai(token):
    #Sets placement to a number that has no affect on the game
    placement = 8

    #Prevents players from playing a Double Trap Horizontally. For Example: 0 0 1 1 1 0 0
    for row in range(0,6):
        for column in range(0,4):
            if board[row][column-1] == 0 and board[row][column] == 1 and board[row][column+1] == 1 and board[row][column+2] == 0 and board[row][column+3] == 0:
                if row != 5 and board[row][column+2] == 0 and board[row+1][column+2] != 0:
                    if token == 1:
                        placement = column + 2
                if row == 5 and board[row][column+2] == 0:
                    if token == 1:
                        placement = column + 2

    for row in range(0,6):
        for column in range(1,5):
            if board[row][column-2] == 0 and board[row][column-1] == 0 and board[row][column+1] == 1 and board[row][column+1] == 1 and board[row][column+2] == 0:
                if row != 5 and board[row][column-1] == 0 and board[row+1][column-1] != 0:
                    if token == 1:
                        placement = column - 1
                if row == 5 and board[row][column-1] == 0:
                    if token == 1:
                        placement = column - 1

    
    #Blocks the Player if they are going to win horizontally. 
    for row in range(0,6):
        for column in range(0,3):
            if board[row][column+1] == token and board[row][column+2] == token and board[row][column+3] == token:
                if row != 5 and board[row][column] == 0 and board[row+1][column] != 0:
                    placement = column
                    
                if row == 5 and board[row][column] == 0:
                    placement = column

            if board[row][column] == token and board[row][column+2] == token and board[row][column+3] == token:
                if row != 5 and board[row][column+1] == 0 and board[row+1][column+1] != 0:
                    placement = column + 1
                    
                if row == 5 and board[row][column+1] == 0:
                    placement = column + 1
                    
            if board[row][column] == token and board[row][column+1] == token and board[row][column+3] == token:
                if row != 5 and board[row][column+2] == 0 and board[row+1][column+2] != 0:
                    placement = column + 2

                if row == 5 and board[row][column+2] == 0:
                    placement = column + 2
 
            if board[row][column] == token and board[row][column+1] == token and board[row][column+2] == token:
                if row != 5 and board[row][column+3] == 0 and board[row+1][column+3] != 0:
                    placement = column + 3

                if row == 5 and board[row][column+3] == 0:
                    placement = column + 3

    #Blocks the Player if they are going to win horizontally from the right wall of the board.
    for row in range(0,6):
        for column in range(6,3,-1):
            if board[row][column] == token and board[row][column-1] == token and board[row][column-2] == token:
                if row != 5 and board[row][column-3] == 0 and board[row+1][column-3] != 0:
                    placement = column - 3

                if row == 5 and board[row][column-3] == 0:
                    placement = column - 3
                    
            if board[row][column] == token and board[row][column-2] == token and board[row][column-3] == token:
                if row != 5 and board[row][column-1] == 0 and board[row+1][column-1] != 0:
                    placement = column - 1

                if row == 5 and board[row][column-1] == 0:
                    placement = column - 1

            if board[row][column-1] == token and board[row][column-2] == token and board[row][column-3] == token:
                if row != 5 and board[row][column] == 0 and board[row+1][column] != 0:
                    placement = column

                if row == 5 and board[row][column] == 0:
                    placement = column

            if board[row][column] == token and board[row][column-1] == token and board[row][column-3] == token: 
                if row != 5 and board[row][column-2] == 0 and board[row+1][column-2] != 0:
                    placement = column - 2
                if row == 5 and board[row][column-2] == 0:
                    placement = column - 2
                    
    #Blocks the Player if they are going to win vertically.              
    for row in range(5,2,-1):
        for column in range(0,7):
            if board[row][column] == token and board[row-1][column] == token and board[row-2][column] == token:
                if board[row-3][column] == 0:
                    placement = column

    #Blocks the Player if they are going to win diagonally. 
    for row in range(0,3):
        for column in range(0,4):
            if board[row+1][column+1] == token and board[row+2][column+2] == token and board[row+3][column+3] == token:
                if board[row][column] == 0 and board[row+1][column] !=0:
                    placement = column
                    
            if board[row][column] == token and board[row+2][column+2] == token and board[row+3][column+3] == token:
                if board[row+1][column+1] == 0 and board[row+2][column+1] != 0:
                    placement = column + 1
                    
            if board[row][column] == token and board[row+1][column+1] == token and board[row+3][column+3] == token:
                if board[row+2][column+2] == 0 and board[row+3][column+2] != 0:
                    placement = column + 2

            if board[row][column] == token and board[row+1][column+1] == token and board[row+2][column+2] == token:
                if row !=2 and board[row+3][column+3] == 0 and board[row+4][column+3] != 0:
                    placement = column + 3
                if row == 2 and board[row+3][column+3] == 0:
                    placement = column + 3
                    
    for row in range(5,3,-1):
       for column in range(0,4):
            if board[row-1][column+1] == token and board[row-2][column+2] == token and board[row-3][column+3] == token:
                if row != 5 and board[row][column] == 0 and board[row+1][column] != 0:
                    placement = column
                if row == 5 and board[row][column] == 0:
                    placement = column

            if board[row][column] == token and board[row-2][column+2] == token and board[row-3][column+3] == token:
                if board[row-1][column+1] == 0 and board[row][column+1] != 0:
                    placement = column + 1

            if board[row][column] == token and board[row-1][column+1] == token and board[row-3][column+3] == token:
                if board[row-2][column+2] == 0 and board[row-1][column+2] != 0:
                    placement = column + 2

            if board[row][column] == token and board[row-1][column+1] == token and board[row-2][column+2] == token:
                if board[row-3][column+3] == 0 and board[row-2][column+3] != 0:
                    placement = column + 3
               
    return placement

#Checks if the computers placement allows the player to win in the next turn. If so it returns true.
def placement_check(placement):
    
    checker = ai(1)
    #If it wins with its placement it does not move its piece.
    if winner(2) == True:
        return False
    #If the player can win in the next turn it returns True.
    if checker != 8:
        return True
    #If the player cannot win in the next turn it returns False.
    if checker == 8:
        return False
    
#Computer that plays with strategy. It blocks the player from winning and looks to see if it can win.
def computer_placer_with_ai():
    global computerturns
    placement = ai(2)
    if placement == 8:
        placement = ai(1)

    #Checks to see if placement is unchanged. If it is a random column is assigned.
    if placement == 8:
        placement = randint(0,6)
    
    #Checks to see if the chosen column is full or not. If it is a random column is assigned.
    while board[0][placement] != 0:
        placement = randint(0,6)
    
    attempts = 0
    while placement_check(placement) == True:
        if attempts >= 7:
            placement = ai(2)
            if placement == 8:
                placement = ai(1)
            break
        placement = randint(0,6)
        while board[0][placement] != 0:
            placement = randint(0,6)
        attempts += 1

    placer(placement, 2)    
                
    #Prints the column the computer choose to place its piece in.
    print("\nComputer Turn "+str(computerturns)+"\nThe Computer Placed The Piece In Column "+ str(placement + 1)+".")
    computerturns += 1
    
#Checks to see if the player or computer has won
def winner(token):

    #Checks to see if someone has won horizontally
    for row in range(0,6):
        for column in range(0,3):
            if board[row][column] == token and board[row][column+1] == token and board[row][column+2] == token and board[row][column+3] == token:
                return True

    for row in range(0,6):
        for column in range(6,5,-1):
            if board[row][column] == token and board[row][column-1] == token and board[row][column-2] == token and board[row][column-3] == token:
                return True
    
    #Checks to see if someone has won vertically
    for row in range(0,3):
        for column in range(0,6):
            if board[row][column] == token and board[row+1][column] == token and board[row+2][column] == token and board[row+3][column] == token:
                return True

    #Checks to see if someone has won diagonally
    for row in range(0,3):
        for column in range(0,4):
            if board[row][column] == token and board[row+1][column+1] == token and board[row+2][column+2] == token and board[row+3][column+3] == token:
                return True

    for row in range(0,3):
        for column in range(6,2,-1):
            if board[row][column] == token and board[row+1][column-1] == token and board[row+2][column-2] == token and board[row+3][column-3] == token:
                return True

#Menu that aks that user what they want to do
def menu_select():
    try:
        menu = int(input("Press [1] to Play\nPress [2] For The Rules\nPress [3] to Exit\n"))
        return menu
    except ValueError:
        print("Invalid Entry\nTry Again")
        return menu_select()

#Game Function - Runs all of the function mentioned above in the appropriate order.
def Game(): 
    boardreset()
    print("\nWelcome to Connect 4")

    menu = menu_select()

    firstprint = 0

    while True:
        if menu == 1:
            if firstprint < 1:
                printboard()
                firstprint += 1
            try:
                user_placement = int(input("Which Column Would You Like To Place A Piece: "))-1
            except:
                print("Numbers Only")
                user_placement = int(input("Which Column Would You Like To Place A Piece: "))-1

            player_placer(user_placement)
            if winner(1) == True:
                printboard()
                print("You Beat the Computer in "+str(playerturns - 1)+" turns.")
                Game()
            computer_placer_with_ai()
            if winner(2) == True:
                printboard()
                print("The Computer Won in "+str(computerturns - 1)+" turns.")
                Game()
            print("\nFree Advice: "+ str(tips[randint(0,3)]))
            printboard()
        
            if 0 not in row1:
                print("Tie Game")
                Game()       
                
        if menu == 2:
            print("\nConnect 4 is a turn-based strategy game that involves placing chips into a 6 by 7 board. The Goal of the game is to be the first person with 4 chips in a row.")
            print("\n-Players take turns placing a chip in one of the 7 avaliable slots.\n\n-If the slot is full the player must select another slot to place their piece.\n\n-Once one of the players has achieved 4 chips in a row either horizontally, diagonally, or vertically the game is over")
            print("\nHave Fun & Enjoy\n")
            menu = menu_select()

        if menu == 3:
            quit()

Game()
