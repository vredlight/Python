def merge(A,B):    # Merge A[0:m] and B[0:n]
  
  (C,m,n) = ([],len(A),len(B))
  (i,j) = (0,0)
  
  while i+j < m+n :  # i+j is the no. of elements merged so far
    if j == n:          # Case 1 : B is empty
      C.append(A[i])
      i = i + 1
    
    elif i ==  m:       # Case 2 : A is empty
      C.append(B[j])
      j = j + 1
    
    elif A[i] <= B[j]:  # Case 3: Element of A is smaller
      C.append(A[i])
      i = i + 1
    
    elif A[i] > B[j]:   # Case 4: Element of B is smaller
      C.append(B[j])
      j = j + 1
  return (C)


def mergeSort(A,left,right):
  
  if right - left <= 1 :     # if the list has 1 or 0 elements return the same string 
    return (A[left:right])
  
  if right - left > 1 :
    mid = (left + right)//2         # recursively calling the mergeSort fn on the left and right half of the list
    L = mergeSort(A,left,mid)
    R = mergeSort(A,mid,right)
    return (merge(L,R))

  