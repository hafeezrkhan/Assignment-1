
# coding: utf-8

## #IMPORT MODULES

# In[1]:


import csv
import pprint
import operator
import os
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
import colorama
from colorama import Fore, Back, Style


## #DRAW DOUBLE DASH LINE

# In[ ]:

str = "=========================================================================================";
print str.title();


## #COLLECT DATA FROM CSV FILE

# In[2]:

array = []
i = 0
print(Fore.RED +"Code Importing Data Records From the CSV File Named: <datagovdatasetsviewmetrics.csv>")
with open('C:\Python27\Scripts\datagovdatasetsviewmetrics.csv') as f:
    reader = csv.reader(f)
    for row in reader:
    	i = i + 1
    	array.append(row)
str = "=========================================================================================";
print str.title();


## #PRINT DATA RESULT FROM CSV FILE

# In[3]:

print(Fore.BLACK + 'Total Number of records imported from CSV File: {}\n'.format(i-1))
#elimination of not needed sets of records to save memory and allow for grouping computation
del array[0]
for item in array:
	del item[4]
	del item[1]
	del item[0]
	item[1] = int(item[1])


## #CREATING GROUP ARRAY

# In[4]:

arrayone = []
for item in array:
	k = 0
	for i in range(0,len(arrayone)):
		if item[0] in arrayone[i][0]:
			arrayone[i][1] = arrayone[i][1] + item[1]
			k = 1
	if k == 0:
		arrayone.append(item)


## #SORT ARRAY IN REVERSE ORDER AND DRAW DOUBLE DASH LINE 

# In[5]:

arrayone = sorted(arrayone, key=operator.itemgetter(1), reverse=True)
str = "=========================================================================================";
print str.title();


## #CREATE ARRAY OF TOP 10 HIGHEST RESULTS

# In[6]:

print(Fore.BLUE + "Top Ten Organization's Result:")
i = 0
toptenarray = []
x = []
y = []
for item in arrayone:
	if i < 10:
		toptenarray.append(item)
		x.append(item[0])
		y.append(item[1])
		i += 1


## #CREATE AND PRETTY PRINT A TABLE TO SHOW THE TOP TEN ORGANIZATION'S RESULT ND DRAW DOUBLE LINE

# In[7]:

print tabulate(toptenarray, tablefmt="fancy_grid")

str = "=========================================================================================";
print str.title();


## #PLOT A BAR CHART BASED ON PRETTY PRINT'S 10 HIGHEST RESULTS 

# In[8]:

print(Fore.RED +"Bar Chart Based on Pretty Print's 10 Highest Results")
bar_width = 0.65
xl = np.arange(len(y))
fig, ax = plt.subplots()
ax.bar(xl, y, width=bar_width, facecolor = 'red')
ax.set_xticks(xl + (bar_width/1.5))
ax.set_xticklabels(x, rotation=30, fontsize=8, horizontalalignment = 'right', verticalalignment = 'top')
plt.show()
os.system("pause") 

str = "=========================================================================================";
print str.title();


# In[ ]:



