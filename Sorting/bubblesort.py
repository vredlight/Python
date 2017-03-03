def bubblesort(l):
  for i in range (len(l)-1):
    for j in range (len(l)-1-i):
      if (l[j+1] <l[j]):
        (l[j+1],l[j]) = (l[j],l[j+1])
  return l