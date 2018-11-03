import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.cbook import get_sample_data
sns.set()


def inlayPlot(x=None,y=None, img=None, x_label=None, y_label=None, x_fit=None, y_fit=None, text_x=None, text_y=None):

    x = np.arange(1, 10, 1)
    y = x**2 + np.random.rand(len(x)) * 3
    
    if x_label == None and y_label == None:
        x_label = 'Test X Label'
        y_label = 'Test Y Label'
    
    if x_fit == None and y_fit == None:
        x_fit = x
        y_fit = x_fit**2
    
    if img == None:
        with get_sample_data('grace_hopper.png') as image: 
            img = plt.imread(image)
            
    
    if text_x == None and text_y == None:
        annotation = dict(s='THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
         xy=(5,25),
         arrowprops=dict(arrowstyle='->'),
         xytext=(6, 1))
        
    
    fig, ax = plt.subplots(1, figsize=(10,10)) 
    
    ax.scatter(x, y, c='g')
    ax.plot(x_fit, y_fit, c='r', linestyle='--')
    ax.annotate(**annotation)
    
    # this is where you can change the size and location of the image
    a = plt.axes([0.2, 0.6, 0.2, 0.2])
    a.imshow(img)
    a.axis('off')
    
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
    return ax, fig