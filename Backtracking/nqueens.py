'''
  # prints one of the possible solution of the nqueens problem
  
  # in nqueens problem, we try to place n queens in n*n board such that no queen attack any other queen
'''

def initialize(n):                                                       
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



def placequeen(i):                                              # places the Ith queen on the board
  n = len(board['queens'].keys())
  for j in range (n):
    if free(i,j):
      addqueen(i,j)
      if i == n-1:
        return (True)
      else:
        extendsol = placequeen(i+1)
      if extendsol:
        return (True)
      else :
        undoqueen(i,j)
  else:
    return(False)


def free(i,j):                                                                                                     # checks if the current block could accomodate the       
  return(board['row'][i]==0 and board['col'][j]==0 and board['nwtose'][j-i]==0 and board['swtone'][j+i]==0)        # specified queen   

def addqueen(i,j):                                                                                               
  board['queens'][i] = j                                                                                           # adds the queen to the specified row and column
  board['row'][i] = 1
  board['col'][j] = 1
  board['nwtose'][j-i] = 1
  board['swtone'][j+i] = 1

def undoqueen(i,j):                                                                                                # undoes the most recently added queen 
  board['queens'][i] = -1
  board['row'][i] = 0
  board['col'][j] = 0
  board['nwtose'][j-i] = 0
  board['swtone'][j+i] = 0

def printboard():                                                                                                  # prints the current status of n*n board
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
initialize(n)
if placequeen(0):
  printboard()
    