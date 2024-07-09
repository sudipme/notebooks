import numpy as np
import matplotlib.pyplot as plt

## LINES

def basicStLine(x1,x2,y1,y2):
    x = np.array([x1,x2]) # X coordinates of the points
    y = np.array([y1,y2]) # Y coordinates of the points
    plt.plot(x,y) # it generates a line from (x1,y1) to (x2,y2)
    plt.show()  # displays the graph

# basicStLine(1,2,3,4) # generates a stline from (1,3) to (2,4)

def multiLine(x1,x2,x3,x4,y1,y2,y3,y4):
    x = np.array([x1,x2,x3,x4])
    y = np.array([y1,y2,y3,y4])
    plt.plot(x,y)
    plt.show()    

#multiLine(1,2,3,4,10,5,9,3)

# if only y values are given then it will assume x values as 0,1,2,3...
def multiLine_y(y1,y2,y3,y4):
    y = np.array([y1,y2,y3,y4])
    plt.plot(y) # x is taken automatically as [0,1,2,3...] according to number of y values
    plt.show() 

#multiLine_y(10,5,9,3)

def lineStyles(y1,y2,y3,y4):
    y = np.array([y1,y2,y3,y4])
    plt.plot(y, linestyle = 'dotted' , color = 'red', linewidth = '10')
    plt.show() 

#lineStyles(10,5,9,3)

def lineStyles_short(y1,y2,y3,y4):
    y = np.array([y1,y2,y3,y4])
    plt.plot(y, ls = ':' , c = 'g', lw = '5')
    plt.show() 

lineStyles_short(10,5,9,3)











