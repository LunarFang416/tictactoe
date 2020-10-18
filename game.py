board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
is_game_on = True
winner = None
player = "X"
counter = 0

def displayboard():
  print("+*********" * 3)
  print("|         |         |         |")
  print("|   ", board[0], "   |   ", board[1], "   |   ", board[2], "   |")
  print("|         |         |         |")
  print("+*********" * 3)
  print("|         |         |         |")
  print("|   ", board[3], "   |   ", board[4], "   |   ", board[5], "   |")
  print("|         |         |         |")
  print("+*********" * 3)
  print("|         |         |         |")
  print("|   ", board[6], "   |   ", board[7], "   |   ", board[8], "   |")
  print("|         |         |         |")
  print("+*********" * 3)

def playgame():
  displayboard()
  
  while is_game_on:
    turn()
  
    isgameover()

    flipturn()

  if winner == "X" or winner == "O":
    print(winner, " has won!")
  elif winner == None:
    print("it has been a tie!")

def turn():
  global player, counter
  print(player + "'s turn.")
  pos = input("What position do you want to place your symbol: ")
  
  while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    pos = input("What position do you want to place your symbol: ")

  pos = int(pos) - 1
  while board[pos] == "X" or board[pos] == "O":
    print("Wrong move! Try Again.")
    pos = input("What position do you want to place your symbol: ")
  
  board[pos] = player
  displayboard()
  counter = counter + 1

def flipturn():
  global player
  if player == "X":
    player = "O"
  elif player == "O":
    player = "X"

def isgameover():
  checkwin()
  checktie()

def checkwin():
  global winner, is_game_on
  row_winner = checkrows()
  column_winner = checkcolumns()
  diagnol_winner = checkdiagnols()
  
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagnol_winner:
    winner = diagnol_winner
  else:
    winner = None
  return winner

def checkrows():
  global is_game_on
  row1 = board[0] == board[1] == board[2] 
  row2 = board[3] == board[4] == board[5]
  row3 = board[6] == board[7] == board[8]
  
  if row1 or row2 or row3:
    is_game_on = False

  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]
  return

def checkcolumns():
  global is_game_on
  column1 = board[0] == board[3] == board[6]
  column2 = board[1] == board[4] == board[7]
  column3 = board[2] == board[5] == board[8]
  
  if column1 or column2 or column3:
    is_game_on = False
  if column1:
    return board[0]
  elif column2:
    return board[1]
  elif column3:
    return board[2]
  return

def checkdiagnols():
  global is_game_on
  diag1 = board[0] == board[4] == board[8]
  diag2 = board[2] == board[4] == board[6]
  
  if diag1 or diag2:
    is_game_on = False
  if diag1:
    return board[0]
  elif diag2:
    return board[2]
  return

def checktie():
  global is_game_on
  if counter == 9 and winner == None:
    is_game_on = False
  
playgame()
