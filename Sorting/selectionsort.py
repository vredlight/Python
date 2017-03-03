# SELECTION SORT

def selectionsort(l):
 # select the smallest element from the slice and place it in it's proper position
 # in each iteration we will select the smallest element from the unsorted elements and place it in it's proper pos..after the sorted slice   
 
  for pos in range (len(l)):
    small = pos
    for i in range (pos,len(l)):
      if l[i]<l[small]:
        small = i
    (l[pos],l[small]) = (l[small],l[pos])
  return (l)