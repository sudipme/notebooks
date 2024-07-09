import numpy as np
import matplotlib.pyplot as plt

## MARKERS (points)

def plotPoints(x1,x2,x3,y1,y2,y3):
    x = np.array([x1,x2,x3])
    y = np.array([y1,y2,y3])
    plt.plot(x,y,'o') # this is a shortcut notation parameter 'o', called marker
    plt.show()

#plotPoints(1,2,3,10,5,9)

"""
Marker Description
'o'	Circle	
'*' Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline	

"""

def lineWithMarkers(y1,y2,y3,y4):
    y = np.array([y1,y2,y3,y4])
    plt.plot(y,marker='o') # x is taken automatically as [0,1,2,3...] according to number of y values
    plt.show() 

#lineWithMarkers(10,5,9,3)


## Format Strings  fmt : ONE LINE SHORTCUT FOR ( MARKER | LINE STYLE | LINE COLOR )

def fmt_demo(y1,y2,y3,y4):
    y = np.array([y1,y2,y3,y4])
    plt.plot(y, 'o:r')  # marker = o , line style = : , line color = red
    plt.show() 

#fmt_demo(10,5,9,3)

"""
'-'	Solid line	
':'	Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line
"""

"""
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White

"""

def markerStyles(y1,y2,y3,y4):
    y = np.array([y1,y2,y3,y4])
    plt.plot(y, marker='o', ms =20, mfc = 'r',mec='g') 
    plt.show() 
    ## ms = marker size, mfc = marker face color, mec = marker edge color
    # we can use hex color code


#markerStyles(10,5,9,3)