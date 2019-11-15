#!/usr/bin/python
import sys
import collections
str1 = list(sys.argv[1])
str2 = list(sys.argv[2])

print("Provided strings are %s and %s" %(sys.argv[1],sys.argv[2]))

def not_ana():
    print("The words are not Anagram words")
    exit()

if len(str1) != len(str2):
    not_ana()

#di = collections.defaultdict(int)
di = {}
for chr in str1:
    if chr in di :
        di[chr] += 1
    else:
        di[chr] = 1 

for chr in str2:
   if chr in di:
       di[chr] = di[chr] - 1
   else:
       not_ana()

for i in di.values():
    if i > 0:
         not_ana()

#if list(di.values()).count(0) == len(str1):
print("The words are ANAGRAM words") 
   
    
  
