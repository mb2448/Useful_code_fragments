from matplotlib import pyplot as plt
import numpy as np

im = plt.imshow(np.random.rand(10,10)*255, interpolation='nearest')
plt.title('Click on this plot to get the values')
fig = plt.gcf()
ax = plt.gca()

class EventHandler:
    def __init__(self):
        fig.canvas.mpl_connect('button_press_event', self.onpress)

    def onpress(self, event):
        if event.inaxes!=ax:
            return
        xi, yi = (int(round(n)) for n in (event.xdata, event.ydata))
        value = im.get_array()[xi,yi]
        color = im.cmap(im.norm(value))
        print( xi,yi,value,color)

handler = EventHandler()

plt.show()
