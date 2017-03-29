
# PROGRAM TO FIND  WHETHER A KNIGHT PLACED ON ANY BLOCK IN A 'M X N' BOARD OF CHESS WILL BE ABLE TO REACH A CERTAIN TARGET BLOCK IN ANY NO. OF MOVES

def neighbours(a,b):
  
  for i in [-1,1]:
    for j in [2,-2]:
      if (a+i <= rlim) and (b+j <= clim) and ( a+i>0) and (b+j>0):
        if ((a+i,b+j) not in list) and ((a+i,b+j) not in marked):
          list.insert(0,(a+i,b+j))
          marked.append((a+i,b+j))
          
      if (b+i <= clim) and (a+j <= rlim) and ( b+i > 0 ) and ( a+j >0):
        if ((a+j,b+i) not in list) and ((a+i,b+j) not in marked):
          list.insert(0,(a+j,b+i))
          marked.append((a+j,b+i))
          
  return (list)


def check(list):
  
  while(list):
   
    list = neighbours(list[0][0],list[0][1]) 
    a = list.pop()
    if a == target:
      print("TARGET REACHED ")
      return  
  print("OOPS..! CAN'T GET THERE ")
  return  

print ("Enter the size of the board ")
rlim = int(input(" Enter the no. of rows  :"))
clim = int(input(" Enter the no. of columns :"))
a = int(input ( " Enter the knight's row pos :"))
b = int(input ( " Enter the knight's column pos  :"))
knight = (a,b)
marked = [knight]

a = int(input ( " Enter the target block's row pos :"))
b = int(input ( " Enter the target block's column pos  :"))
target = (a,b)

list = [(knight[0],knight[1])]
check(list)    