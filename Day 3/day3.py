# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:29:41 2020

@author: Marc
"""

#open input
alllines = []
with open(r"Day3.txt","r") as f:
	for line in f.readlines():
		alllines.append(line.rstrip())

def counttrees(input, right, down):
    """ counts the trees in a slope, for Advent of Code 2020, day 3
    Keyword :
    input -- a list of strings, corresponding to the "slope"
    right -- the number of position the sledge moves to the right
    down -- the number of positions the sledge moves down 
    """
    #select the rows we want according to how many steps down we take each time
    input2 = []
    for i in range(0, len(input)): 
        if i == 0:
            input2.append(input[i])
        elif i % down == 0: 
            input2.append(input[i]) 
        else : 
            pass 
    #adjust string length according to right steps so we can get to the bottom
    K = len(input2)*right
    input3 = []
    for line in input2:
        line = (line * (K//len(line)+ 1))[:K]
        input3.append(line)
    #count the trees we crash against!
    trees = 0
    i = 0
    for line in input3:
        if line[i] == "#":
            trees = trees + 1
        else:
            pass
        i = i + right
    return trees

#Part 1

trees3 = counttrees(alllines, 3, 1)

#Part 2
trees1 = counttrees(alllines, 1, 1)
trees5 = counttrees(alllines, 5, 1)
trees7 = counttrees(alllines, 7, 1)
trees12 = counttrees(alllines, 1, 2)

result = trees3*trees1*trees12*trees5*trees7