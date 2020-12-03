# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:38:37 2020

@author: Marc
"""
#open input
alllines = []
with open(r"C:\Users\Marc\Documents\GitHub\AdventOfCode\AdventOfCode2020\Day 3/Day3.txt","r") as f:
	for line in f.readlines():
		alllines.append(line.rstrip())

#Part 1

#get each row to the right length
        
K = (len(alllines)*3)
longlines = []
for line in alllines:
    line = (line * (K//len(line)+ 1))[:K]
    longlines.append(line)

#count those damn trees

trees3 = 0

i = 0

for line in longlines:
        if line[i] == "#":
            trees3 = trees3 + 1
        else:
            pass
        i = i +3

#Part 2
        
#Right one down one

K = (len(alllines))
longlines = []
for line in alllines:
    line = (line * (K//len(line)+ 1))[:K]
    longlines.append(line)        

i=0
trees1 = 0
for line in longlines:
        if line[i] == "#":
            trees1 = trees1 + 1
        else:
            pass
        i = i +1
        
#Right five one down
        
K = (len(alllines)*5)
longlines = []
for line in alllines:
    line = (line * (K//len(line)+ 1))[:K]
    longlines.append(line)        

i=0
trees5 = 0
for line in longlines:
        if line[i] == "#":
            trees5 = trees5 + 1
        else:
            pass
        i = i + 5
        
#Right seven one down
        
K = (len(alllines)*7)
longlines = []
for line in alllines:
    line = (line * (K//len(line)+ 1))[:K]
    longlines.append(line)        

i=0
trees7 = 0
for line in longlines:
        if line[i] == "#":
            trees7 = trees7 + 1
        else:
            pass
        i = i +7

#Right one one downdown two
        
K = (len(alllines))
longlines = []
for line in alllines:
    line = (line * (K//len(line)+ 1))[:K]
    longlines.append(line)        

#keep only even indexed lines
    
evenlines = []

for i in range(0, len(longlines)): 
    if i == 0:
        evenlines.append(longlines[i])
    elif i % 2 == 0: 
        evenlines.append(longlines[i]) 
    else : 
        pass 
  

i=0
trees12 = 0
for line in evenlines:
        if line[i] == "#":
            trees12 = trees12 + 1
        else:
            pass
        i = i +1

result = trees1*trees12*trees3*trees5*trees7