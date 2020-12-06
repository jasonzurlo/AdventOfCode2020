# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:51:02 2020

@author: Marc
"""

#open input

with open(r"day6.txt","r") as f:
	forms = f.readlines()

#Part 1: get all questions in which anyone answered "yes"
#dump each line in a string
forms2 = ""

for line in forms:
    forms2 = forms2 + line

#make list with each passport as an item
    
forms3 = forms2.split("\n\n")

#get the number of unique characters in each group
lengths = []

for line in forms3:
    unique = "".join(set(line)).replace("\n","")
    length = len(unique)
    lengths.append(length)
    
#get the total number of"yes" answers
import numpy as np

lengths = np.array(lengths)

result = lengths.sum()

#Part 2: get all questions in which everyone answered "yes"

forms4 = []
#find the number of 
for form in forms3:
    formlist = form.split("\n")
    forms4.append(formlist)

items = []

for form in forms4:
    its = len(form)
    items.append(its)
frequences = []

for form in forms3:
    freq = {}
    for char in form:
        if char in freq:
            freq[char] +=1
        else:
            freq[char] = 1
    frequences.append(freq)

everyones = []

for i in range(0,502):
    everyone = sum(1 for value in frequences[i].values() if value == items[i])
    everyones.append(everyone)


result2 = sum(np.array(everyones))