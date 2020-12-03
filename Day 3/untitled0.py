# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:38:37 2020

@author: Marc
"""
#open input
alllines = []
with open("Day3.txt","r") as f:
	for line in f.readlines():
		alllines.append(line.rstrip())

#get each row to the right length
        
K = (len(alllines)*3)



trees = 0

i = 0

for line in alllines:
    try:
        if line[i*3] == "#":
            trees = trees + 1
        else:
            pass
        i = i +1
    except IndexError:
        i = 0
        if line[i*3] == "#":
            trees = trees + 1
        else:
            pass
        i = i +1