

# bubble sort 

def bubble_sort(array):

    size =len(array)-1

    for i in range(size):
      
      swap = False
      
      for j in range(size-i):

        if array[j]>array[j+1]:
           array[j],array[j+1]=array[j+1],array[j]
           swap=True
        
      if not swap:
          return array
         

    return array

result = bubble_sort([8,1,3,9,20,11,0,-1,30,-1,0])

print(result)