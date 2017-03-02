# Insertion Sorting 
def insertionSort(list):
  # start building sorted slices by adding one element at a time 
  # after each iteration slice[0:sliceEnd] is already sorted
  # in each iteration we put the new element at its right place in the already sorted slice

  for sliceEnd in range(len(list)):
    pos = sliceEnd
    while (pos>0 and list[pos] < list[pos-1]):
      (list[pos],list[pos-1]) = (list[pos-1],list[pos])
      pos = pos -1
  return(list)