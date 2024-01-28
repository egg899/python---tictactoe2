from random import randrange
 

numsBoard =[[1,2,3],[4,'X',6],[7,8,9]]
#OTHER WAY TO MAKE THE BOARD WITH 'X' IN THE MIDDLE
#board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
#board[1][1] = 'X' # set first 'X' in the middle

##def display_board(board):
##    for i in range(3):
##        print('-----')
##        for j in range(3):
##            print(board[i][j], end="|")
##        print('')    
##    print('-----')

def display_board(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

display_board(numsBoard)


cross = "X"
circle = "O"
computer = ""
user = ""

computer = cross
user = circle




def enter_move(board):
    global play, row, col, sign
    
   
    while True:
        try:
            play = int(input('Enter your move: '))
            row = (play - 1) // 3
            col = (play - 1) % 3

            if 1<= play <= 9 and numsBoard[row][col] not in ["X", "O"]:
                break
            else:
                print("Invalid choice. Please choose an available box.")
                
        except ValueError:
             print("Invalid input. Please enter a number between 1 and 9")



    if play == 1:
        numsBoard[0][0] = user
        display_board(board)
    
    if play == 2:
        numsBoard[0][1] = user
        display_board(board)

    if play == 3:
        numsBoard[0][2] = user
        display_board(board)

    if play == 4:
        numsBoard[1][0] = user
        display_board(board)

    if play == 5:
        numsBoard[1][1] = user
        display_board(board)

    if play == 6:
        numsBoard[1][2] = user
        display_board(board)

    if play == 7:
        numsBoard[2][0] = user
        
        display_board(board)

    if play == 8:
        numsBoard[2][1] = user
        
        display_board(board)

    if play == 9:
        numsBoard[2][2] = user
        
        display_board(board)




       
compChoices=[]
rounds_played = 0
max_rounds = 4

def make_list_of_free_fields(board):
    global free_fields
    free_fields = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] not in ["X", "O"]:
                free_fields.append((row, col))
                
                compChoices.append(board[row][col])
                

                
    #print(free_fields)
        
            


def victory_for(board, sign='O'):
    winMap = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [3,5,7], [1,5,9]]
    fields = []
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == sign:
                    number = (row * 3) + col + 1
                    fields.append(number)
            
##                if (row, col)==(0, 0):
##                    fields.append(1)
##                if (row, col)==(0, 1):
##                    fields.append(2)
##                if (row, col)==(0, 2):
##                    fields.append(3)
##                if (row, col)==(1, 0):
##                    fields.append(4)
##                if (row, col)==(1, 1):
##                    fields.append(5)
##                if (row, col)==(1, 2):
##                    fields.append(6)
##                if (row, col)==(2, 0):
##                    fields.append(7)
##                if (row, col)==(2, 1):
##                    fields.append(8)
##                if (row, col)==(2, 2):
##                    fields.append(9)    
                
            
##    print("fields", fields)
    for win_combo in winMap:
        
        if (set(win_combo).intersection(set(fields)) == set(win_combo)):
            return True
    return False       
            
       

    
   
def draw_move(board):
    random = randrange(len(compChoices))

    user=computer
    play = compChoices[random]
    if play == 1:
        numsBoard[0][0] = user
        display_board(board)
    
    if play == 2:
        numsBoard[0][1] = user
        display_board(board)

    if play == 3:
        numsBoard[0][2] = user
        display_board(board)

    if play == 4:
        numsBoard[1][0] = user
        display_board(board)

    if play == 5:
        numsBoard[1][1] = user
        display_board(board)

    if play == 6:
        numsBoard[1][2] = user
        display_board(board)

    if play == 7:
        numsBoard[2][0] = user
        display_board(board)

    if play == 8:
        numsBoard[2][1] = user
        display_board(board)

    if play == 9:
        numsBoard[2][2] = user
        display_board(board)

    
    
    
   
    
 
    
user = circle
computer = cross

while rounds_played <= max_rounds:
    
    enter_move(numsBoard)
    
    
    
    make_list_of_free_fields(numsBoard)
##    print('free', len(free_fields))
    draw_move(numsBoard)
    compChoices.clear()
    rounds_played +=1
##    print(rounds_played)

    
    if victory_for(numsBoard, user):
        print(f"You won!")
        break
    
    if victory_for(numsBoard, computer):
        print(f"Computer won!")
        break

    if(rounds_played == max_rounds) and (victory_for(numsBoard, user)== False and victory_for(numsBoard, computer)== False) :
         print(f"It's a tie my friend!")
         rounds_played = 0
         break
         
    

    
    
    
    

