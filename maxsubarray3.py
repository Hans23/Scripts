#
#Description: Find the max sum of a sub array
#
#

l = [8,-19,5,-4,20]

high = sum(l)
i = 0
j = len(l) - 1
while i <= j:
   si = i
   while si <= j:
      y = sum(l[i:si+1])
      if y > high: 
           high = y
      si += 1    
   i += 1


print("The highest sum is %d " %(high))


