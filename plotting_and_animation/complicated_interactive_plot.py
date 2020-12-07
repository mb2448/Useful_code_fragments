import time
import numpy as np
import matplotlib.pyplot as plt

def get_peak_value(x):
    #fix this
    return np.max(x)

def get_strehl(x):
    #fix this
    return 1-np.std(x)**2

def get_latest_image():
    #fix this
    return np.random.random((10, 10))

if __name__ == "__main__":
    imshow_params = {'interpolation':'nearest',
                     'origin':'lower'}
    
    ideal_image = np.random.random((10, 10))
    zero_image = np.zeros(ideal_image.shape)
    N_iterations = 100
    
    plt.ion()
    fig = plt.figure(figsize = (8, 8))
    ax1 =plt.subplot2grid((4,4),(0, 0), rowspan =2, colspan = 2)
    ax2 = plt.subplot2grid((4,4),(0, 2), rowspan =2, colspan = 2)
    ax3 =plt.subplot2grid((4,4),(2, 0), rowspan =3, colspan = 2)
    ax4 =plt.subplot2grid((4,4),(2, 2), rowspan =3, colspan = 2)
    
    #Plot titles/axis labels
    title = fig.suptitle('FFWFS')
    ax1.set_title('Current Image')
    ax2.set_title('Perfect PSF')
    ax3.set_title('Peak counts')
    ax4.set_title('Strehl metric')
    ax3.set_xlabel('Iteration')
    ax4.set_xlabel('Iteration')
    
    w1 = ax1.imshow(zero_image, **imshow_params)
    w2 = ax2.imshow(ideal_image, **imshow_params)
    w3, = ax3.plot([],[]); ax3.set_xlim(0, N_iterations)
    w4, = ax4.plot([],[]); ax4.set_xlim(0, N_iterations)
    plt.tight_layout()
    plt.show()
    
    #remove ticks and such from images (optional)
    for w in w1, w2:
        w.axes.get_xaxis().set_visible(False)
        w.axes.get_yaxis().set_visible(False)
         
    itcounter = []
    peakvals = []
    strehls = []
    for i in range(N_iterations):
        itcounter.append(i)
        current_image = get_latest_image()
        
        peakval = get_peak_value(current_image)
        peakvals.append(peakval)
        
        strehl = get_strehl(current_image)
        strehls.append(strehl)
        #update plot here 
        w1.set_data(current_image); w1.autoscale()
        w2.set_data(ideal_image); w2.autoscale()
        w3.set_data(itcounter, peakvals)
        w4.set_data(itcounter, strehls)
        plt.draw()
        plt.pause(0.001)
    plt.ioff()
