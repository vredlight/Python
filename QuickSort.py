import random
def randomize(l):
  for i in range (len(l)//2):
    j = random.randrange(0,len(l),1)
    k = random.randrange(0,len(l),1)
    (l[j],l[k]) = (l[k],l[j])

def QuickSort(A,l,r):
  
  if r - l <= 1 :
    return ()
  
  yellow = l + 1
  
  for green in range (l+1,r):
    if A[green] <= A[l] :
      (A[green],A[yellow]) = (A[yellow],A[green])
      yellow = yellow + 1
  
  (A[l],A[yellow -1 ]) = (A[yellow - 1],A[l])
  
  QuickSort(A,l,yellow-1)
  QuickSort(A,yellow,r)