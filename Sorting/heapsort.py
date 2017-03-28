
def heapify(list):
  last = len(list)
  nodes = (last-1)//2
  for i in range (nodes,-1,-1):
    list = checkheap(i,list)
    
  return (list)


def checkheap(pos,list):
  lchild = (2*pos) +1
  rchild = 2* (pos+1)
  max = len(list)
  if( lchild < max and rchild < max):
    if( list[pos] < list[lchild] and list[pos] < list[rchild]):
      if ( list[lchild] > list[rchild] ):
        ( list[pos],list[lchild] ) = ( list[lchild],list[pos] )
        list = checkheap(lchild,list)
      else:
        ( list[pos],list[rchild] ) = ( list[rchild],list[pos] )
        list = checkheap(rchild,list)  
    elif(list[pos] < list[rchild]):
      ( list[pos],list[rchild] ) = ( list[rchild],list[pos] )
      list = checkheap(rchild,list)
    elif(list[pos] < list[lchild]):
      ( list[pos],list[lchild] ) = ( list[lchild],list[pos] )
      list = checkheap(lchild,list) 
  elif ( lchild < max ):
    if (list[pos] <list[lchild]):
      ( list[pos],list[lchild] ) = ( list[lchild],list[pos] )
      list = checkheap(lchild,list)
  else :
    if ( list[pos] < list[rchild] ):
      ( list[pos],list[rchild] ) = ( list[rchild],list[pos] )
      list =  checkheap(rchild,list) 
    
  return (list)

def delete_max(heap):
  ( heap[0],heap[-1]) = (heap[-1],heap[0])
  heapify(heap[0:len(heap)-1])
  return heap