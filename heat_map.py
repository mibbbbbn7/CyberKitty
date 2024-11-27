import numpy as np
import matplotlib.pyplot as plt 
  
def heat_map(array_x, array_y):
    data = (array_x, array_y) 
    plt.imshow( array_x, array_y ) 
  
    plt.title( "2-D Heat Map" ) 
    plt.show()