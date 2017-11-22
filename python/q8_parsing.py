# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd
import numpy as np

def find_nearest_index(col, value):
    idx = (np.abs(col-value)).argmin()
    return idx

#Import CSV
df = pd.read_csv('/Users/williamstokvis/ds/metis/metisgh/prework/dsp/python/football.csv')
#Create Column with Goal Differential
df['Goal Differential']= df["Goals"]-df['Goals Allowed']
#Find Goal Differential
gd = 0
x = find_nearest_index(df['Goal Differential'],gd)
#Display team
print(df['Team'][x] + ' has the smallest goal differential')