

def initialize(board,n):
  for keys in ['queens','row','col','nwtose','swtone']:
    board[keys] = {}
  for i in range(n):
    board['queens'][i] = -1
    board['row'][i] = 0
    board['col'][i] = 0

  for i in range(-(n-1),n):
    board['nwtose'][i] = 0
  for i in range(2*n-1):
    board['swtone'][i] = 0
def placequeen(i,board):
  n = len(board['queens'].keys())
  for j in range (n):
    if free(i,j,board):
      addqueen(i,j,board)
      if i == n-1:
        return (True)
      else:
        extendsol = placequeen(i+1,board)
      if extendsol:
        return (True)
      else :
        undoqueen(i,j,board)
  else:
    return(False)

def free(i,j,board):
  return(board['row'][i]==0 and board['col'][j]==0 and board['nwtose'][j-i]==0 and board['swtone'][j+i]==0)

def addqueen(i,j,board):
  board['queens'][i] = j
  board['row'][i] = 1
  board['col'][j] = 1
  board['nwtose'][j-i] = 1
  board['swtone'][j+i] = 1

def undoqueen(i,j,board):
  board['queens'][i] = -1
  board['row'][i] = 0
  board['col'][j] = 0
  board['nwtose'][j-i] = 0
  board['swtone'][j+i] = 0

def printboard(board):
  for i in range (n):
    print("|",end="")
    for j in range (n):
      if (board['queens'][i] == j):
        print(" Q |",end="")
      else:
        print(" * |",end="")
    print("")
  
board = {}
n = int(input("How many Queens...?"))
initialize(board,n)
if placequeen(0,board):
  printboard(board)
    