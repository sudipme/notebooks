import numpy as np
import matplotlib.pyplot as plt
def markerStyles(y1,y2,y3,y4):
    y = np.array([y1,y2,y3,y4])
    plt.plot(y, marker='o', ls='--',c='g',ms =10, mfc = 'r',mec='b') 
    plt.title("Title of the Plot")
    plt.xlabel(" X axis")
    plt.ylabel("Y axis")
    plt.show() 

markerStyles(10,5,9,3)