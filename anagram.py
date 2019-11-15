#!/usr/bin/python
import sys
str1 = list(sys.argv[1])
str2 = list(sys.argv[2])

print("Provided strings are %s and %s" %(sys.argv[1],sys.argv[2]))

def not_ana():
    print("The words are not Anagram words")
    exit()

if len(str1) == len(str2):
    for a in str1:
       if str1.count(a) == str2.count(a):
          pass 
       else:
          not_ana()
else:
    not_ana()

print("The words are ANAGRAM words") 
   
    
  
