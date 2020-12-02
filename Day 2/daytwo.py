# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:31:54 2020

@author: Marc
"""
#import libraries
import pandas as pd
import re

#read input
alllines = []
with open("day2.txt","r") as f:
	for line in f.readlines():
		alllines.append(line.rstrip())


#Part 1

     
#create empty lists

minNums = []
maxNums = []
letters = []
passwords = []

for line in alllines:
    minregex = re.compile(r"(\d){1,2}(-)")
    minNum = minregex.search(line).group()
    minNum = minNum[:-1]
    minNums.append(minNum)
    maxregex = re.compile(r"(-)(\d){1,2}")
    maxNum = maxregex.search(line).group()
    maxNum = maxNum[1:]
    maxNums.append(maxNum)
    letterregex = re.compile(r"( )(\w)(:)")
    letter = letterregex.search(line).group()
    letter = letter[1]
    letters.append(letter)
    passwordregex = re.compile(r"(: )(\w)*")
    password = passwordregex.search(line).group()
    password = password[2:]
    passwords.append(password)

#put lists in a table
dfdict = {"Minimum": minNums, "Maximum": maxNums, "Letter": letters, "Password": passwords}

df = pd.DataFrame.from_dict(dfdict)

#change column types
df["Minimum"] = df["Minimum"].astype("int")
df["Maximum"] = df["Maximum"].astype("int")

#for loop to determine whether password is valid or not
lengths = []

for i in range(0, 1000):
    length = passwords[i].count(letters[i])
    lengths.append(length)
lengths = {"Instances": lengths}
lengths = pd.DataFrame.from_dict(lengths)
df = pd.concat([df, lengths], axis = 1)

largers = []
smallers = []

for i in range (0,1000):
    if df["Instances"][i] > df["Maximum"][i]:
        toolarge = "Yes"
    else:
        toolarge = "No"
    largers.append(toolarge)
    if df["Instances"][i] < df["Minimum"][i]:
        toosmall = "Yes"
    else:
        toosmall = "No"
    smallers.append(toosmall)

largeandsmall = {"Too large": largers, "Too small": smallers}

largeandsmall = pd.DataFrame.from_dict(largeandsmall)

df = pd.concat([df, largeandsmall], axis = 1)

isvalid = []

for i in range (0, 1000):
    if (df["Too large"][i] == "Yes") or (df["Too small"][i] == "Yes"):
        valid = "No"
    else:
        valid = "Yes"
    isvalid.append(valid)

isvalid = {"Valid password": isvalid}
isvalid = pd.DataFrame.from_dict(isvalid)

df = pd.concat([df, isvalid], axis = 1)

print(list(isvalid["Valid password"]).count("Yes"))


#part Two

#remove unnecessary columns from the table and change column names

df2 = df[["Minimum", "Maximum", "Letter", "Password"]]

df2.columns = ["Position 1", "Position 2", "Letter", "Password"]

# check if either 1st or 2nd position corresponds to letter

eithers = []

for i in range(0, 1000):
    pos1 = df2["Position 1"][i] -1
    pos2 = df2["Position 2"][i] -1
    if (df2["Password"][i][pos1] == df2["Letter"][i]) or (df2["Password"][i][pos2] == df2["Letter"][i]):
        either = "Yes"
    else:
        either = "No"
    eithers.append(either)

eithers = {"Either": eithers}
eithers = pd.DataFrame.from_dict(eithers)

df2 = pd.concat([df2, eithers], axis = 1)

# check if both 1st or 2nd position correspond to letter


boths = []

for i in range(0, 1000):
    pos1 = df2["Position 1"][i] -1
    pos2 = df2["Position 2"][i] -1
    if (df2["Password"][i][pos1] == df2["Letter"][i]) and (df2["Password"][i][pos2] == df2["Letter"][i]):
        both = "Yes"
    else:
        both = "No"
    boths.append(both)

boths = {"Both": boths}
boths = pd.DataFrame.from_dict(boths)

df2 = pd.concat([df2, boths], axis = 1)

#check if the two conditions for correct apply
valids = []
for i in range(0, 1000):
    if df2["Either"][i] == "No":
        valid = "No"
    elif (df2["Either"][i] == "Yes") and (df2["Both"][i] == "Yes"):
        valid = "No"
    else:
        valid = "Yes"
    valids.append(valid)

valids = {"Valid password": valids}
valids = pd.DataFrame.from_dict(valids)

df2 = pd.concat([df2, valids], axis = 1)
print(list(valids["Valid password"]).count("Yes"))