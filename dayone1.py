# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:01:24 2020

@author: Marc
"""

import pandas as pd


numbers = pd.read_clipboard()
solution = []
for number in numbers["numbers"]:
    for i in range(0,200):
        if number+numbers["numbers"][i] == 2020:
            solution.append([number,numbers["numbers"][i]])
        else:
            pass

import numpy as np

solution2 = np.array(solution[0])

print(solution2[0]*solution2[1])