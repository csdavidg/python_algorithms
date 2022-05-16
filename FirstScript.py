
def largest_two(A):
    maxValues = [A[0], A[0]]
    
    for val in A:
        if val > maxValues[1]:
            maxValues[0] = maxValues[1]
            maxValues[1] = val
    
    return maxValues

def largest_two_book(A):
  my_max,second = A[:2]                
  if my_max < second:
    my_max,second = second,my_max

  for idx in range(2, len(A)):
    if my_max < A[idx]:                
      my_max,second = A[idx],my_max
    elif second < A[idx]:              
      second = A[idx]
  return (my_max, second)

def sorting_two(A):
  return tuple(sorted(A, reverse=True)[:2])    

def double_two(A):
  my_max = max(A)                              
  copy = list(A)
  copy.remove(my_max)
  return (my_max, max(copy))

def mutable_two(A):
  idx = max(range(len(A)), key=A.__getitem__)
  my_max = A[idx]                              
  del A[idx]
  second = max(A)                              
  A.insert(idx, my_max)                        
  return (my_max, second)



largestVal = largest_two([1,2,3,5])

print(largestVal)