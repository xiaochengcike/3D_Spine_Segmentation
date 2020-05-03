"""
===================
Image Slices Viewer
===================

Scroll through 2D image slices of a 3D array.
"""

import numpy as np
import matplotlib.pyplot as plt



def show_3d_images( input_matrix ):

    fig, figure_axes = plt.subplots( 1 , 1 )
    tracker = IndexTracker( figure_axes , input_matrix ) 
    fig.canvas.mpl_connect( 'scroll_event' , tracker.onscroll )
    
    mng = plt.get_current_fig_manager()
    
    # mng.window.state('zoomed')
    mng.window.showMaximized()

    plt.show() 



class IndexTracker(object):
    def __init__(self, ax, X):
        self.ax = ax
        ax.set_title('use scroll wheel to navigate images')

        self.X = X
        rows, cols, self.slices = X.shape

        # self.ind = self.slices//2
        self.ind = 1

        self.im = ax.imshow(self.X[:, :, self.ind] , cmap='gray',vmin=0,vmax=255)
        self.update()

    def onscroll(self, event):
        # print("%s %s" % (event.button, event.step))
        
        if event.button == 'up':
            self.ind = (self.ind + 1) % self.slices
        else:
            self.ind = (self.ind - 1) % self.slices
        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.ind])
        self.ax.set_ylabel('slice %s' % self.ind)
        self.im.axes.figure.canvas.draw()
