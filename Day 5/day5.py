# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:14:59 2020

@author: Marc
"""



#open input

with open(r"day5.txt","r") as f:
	tickets = f.readlines()

#Part 1
#get the position of each ticket

rows = []
columns = []
for ticket in tickets:
    row = 0
    column = 0
    if ticket[0] == "B":
        row = row + 64
    else:
        row = row
    if ticket[1] == "B":
        row = row + 32
    else:
        row = row
    if ticket[2] == "B":
        row = row + 16
    else:
        row = row
    if ticket[3] == "B":
        row = row + 8
    else:
        row = row
    if ticket[4] == "B":
        row = row + 4
    else:
        row = row
    if ticket[5] == "B":
        row = row + 2
    else:
        row = row
    if ticket[6] == "B":
        row = row + 1
    else:
        row = row
    rows.append(row)
    if ticket[7] == "R":
        column = column + 4
    else:
        column = column
    if ticket[8] == "R":
        column = column + 2
    else:
        column = column
    if ticket[9] == "R":
        column = column + 1
    else:
        column = column
    columns.append(column)

#get ticket IDs
    
ids = []

for i in range(0,824):
    idi = (rows[i]*8)+columns[i]
    ids.append(idi)

print(max(ids))

ids = sorted(ids)

#Part 2
#find my seat ticket

for i in range(0,824):
    if ids[i+1] == ids[i] + 1:
        pass
    else:
        print("Your ticket ID is "+str(ids[i]+1))
        break