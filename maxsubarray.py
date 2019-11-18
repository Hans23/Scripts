#
#Description: Find the max number when you sum the sub array in a list
#
#
l = [8,-19,5,-4,20]
result , curr = float("-inf"), float("-inf")
for x in l:
   print ("x = %f" %x)
   curr = max(curr+x,x)
   result = max(result,curr)
   print("curr = %f and result = %f" %(curr,result))
print("The highest sum is %f " %(result))


