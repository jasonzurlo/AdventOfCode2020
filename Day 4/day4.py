# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:34:27 2020

@author: Marc
"""
import re
import pandas as pd

#open input

with open(r"day4.txt","r") as f:
	passports = f.readlines()

#Part 1
#dump each line in a string
passports2 = ""

for line in passports:
    passports2 = passports2 + line

#make list with each passport as an item
    
passports3 = passports2.split("\n\n")


#create regex patterns to check for each item
byrRegex = re.compile(r"byr")
iyrRegex = re.compile(r"iyr")
eyrRegex = re.compile(r"eyr")
hgtRegex = re.compile(r"hgt")
hclRegex = re.compile(r"hcl")
pidRegex = re.compile(r"pid")
eclRegex = re.compile(r"ecl")

#create empty lists where we will check whether the pattern exists

byrs = []
iyrs = []
eyrs = []
hgts = []
hcls = []
pids = []
ecls = []

#loop through passports and check whether patterns exist

for passport in passports3:
    if byrRegex.search(passport) == None:
        byr = "no"
    else:
        byr = "yes"
    byrs.append(byr)
    if iyrRegex.search(passport) == None:
        iyr = "no"
    else:
        iyr = "yes"
    iyrs.append(iyr)
    if eyrRegex.search(passport) == None:
        eyr = "no"
    else:
        eyr = "yes"
    eyrs.append(eyr)
    if hgtRegex.search(passport) == None:
        hgt = "no"
    else:
        hgt = "yes"
    hgts.append(hgt)
    if hclRegex.search(passport) == None:
        hcl = "no"
    else:
        hcl = "yes"
    hcls.append(hcl)
    if pidRegex.search(passport)  == None:
        pid = "no"
    else:
        pid = "yes"
    pids.append(pid)
    if eclRegex.search(passport) == None:
        ecl = "no"
    else:
        ecl = "yes"
    ecls.append(ecl)

#group passports with results in a df and remove invalid ones    
results = {"passport": passports3, "byr": byrs, "iyr": iyrs, "eyr": eyrs, "hgt": hgts, "hcl": hcls, "pid": pids, "ecl": ecls}

results = pd.DataFrame.from_dict(results)

resultsyes = results[(results["byr"] == "yes") & (results["iyr"]== "yes") & (results["eyr"] == "yes") & (results["hgt"] == "yes") & (results["hcl"]== "yes") & (results["pid"] == "yes") & (results["ecl"] == "yes")]

#Part two
#separate valid passports
validpassports = resultsyes["passport"]

#create new regex objects

byrRegex = re.compile(r"(byr:)(\d\d\d\d)")
iyrRegex = re.compile(r"(iyr:)(\d\d\d\d)")
eyrRegex = re.compile(r"(eyr:)(\d\d\d\d)")   
hgtRegex = re.compile(r"(hgt:)(\d){2,3}(\w\w)")
hclRegex = re.compile(r"(hcl:)(#)([0123456789abcdef]){6}(\s)")
pidRegex = re.compile(r"(pid:)([0123456789]){9}")
eclRegex = re.compile(r"(ecl:)(\w\w\w)")

byrs = []
iyrs = []
eyrs = []
hgts = []
hcls = []
pids = []
ecls = []

for passport in validpassports:
    if byrRegex.search(passport) == None:
        byr = "no"
    else:
        byr = byrRegex.search(passport).group()
        byr = int(byr[4:8])
    byrs.append(byr)
    if iyrRegex.search(passport) == None:
        iyr = "no"
    else:
        iyr = iyrRegex.search(passport).group()
        iyr = int(iyr[4:8])
    iyrs.append(iyr)
    if eyrRegex.search(passport) == None:
        eyr = "no"
    else:
        eyr = eyrRegex.search(passport).group()
        eyr = int(eyr[4:8])
    eyrs.append(eyr)
    if hgtRegex.search(passport) == None:
        hgt = "no"
    else:
        hgt = hgtRegex.search(passport).group()
        if hgt[-1] == "\n":
            hgt = hgt[4:].strip("\n")
        else:
            hgt = hgt[4:]
    hgts.append(hgt)
    if hclRegex.search(passport) == None:
        hcl = "no"
    else:
        hcl = hclRegex.search(passport).group()
        hcl = hcl[4:11]
    hcls.append(hcl)
    if pidRegex.search(passport) == None:
        pid = "no"
    else:
        pid = pidRegex.search(passport).group()
        pid = pid[4:13]
    pids.append(pid)
    if eclRegex.search(passport) == None:
        ecl = "no"
    else:
        ecl = eclRegex.search(passport).group()
        ecl = ecl[4:7]
    ecls.append(ecl)
    
#group passports with results in a df and remove invalid ones    
results2 = {"passport": validpassports, "byr": byrs, "iyr": iyrs, "eyr": eyrs, "hgt": hgts, "hcl": hcls, "pid": pids, "ecl": ecls}

results2 = pd.DataFrame.from_dict(results2)

#filter for byr

results2 = results2[(results2["byr"] >= 1920) & (results2["byr"] <= 2002)]

#filter for iyr

results2 = results2[(results2["iyr"] >= 2010) & (results2["iyr"] <= 2020)]

#filter for eyr

results2 = results2[(results2["eyr"] >= 2020) & (results2["eyr"] <= 2030)]

#filter for hcl

results2 = results2[results2["hcl"] !="no"]

#filter for pid
results2 = results2[results2["pid"] !="no"]

#filter for ecl

results2 = results2[results2["ecl"].isin(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])]

#filter for hgt

results2 = results2[results2["hgt"] !="no"]

hgtfilter = []

for hgt in results2["hgt"]:
    if str(hgt)[-2:] == "in":
        hgt = int(str(hgt)[:-2])
        if 59 <= hgt <= 76:
            hgtf = "yes"
        else:
            hgtf = "no"
    else:
        hgt = int(str(hgt)[:-2])
        if 150 <= hgt <= 193:
            hgtf = "yes"
        else:
            hgtf = "no"
    hgtfilter.append(hgtf)
    
results2["hgtfilter"] = hgtfilter

results2 = results2[results2["hgtfilter"] !="no"]
