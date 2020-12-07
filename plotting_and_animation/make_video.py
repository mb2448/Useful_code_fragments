import os
import matplotlib.pyplot as plt
import time
import numpy as np
import gc
import string
import random

def random_str_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_data(datasize):
    x=np.arange(datasize)
    y=x**2*(1+np.random.random(datasize)*0.1)
    return x, y

random_prefix= random_str_generator(4)
datasize = 100
frames = 50
fps=str(10)

#create output directory
outputdir = os.path.join(os.getcwd(),'animation')
if not os.path.exists(outputdir):
    os.system('mkdir '+outputdir)

#Generate some random frames
#while avoiding memory leak in matplotlib
fig = plt.figure()
ax = fig.add_subplot(111)
l1, = ax.plot(*random_data(datasize), antialiased=True)
#for images:
#im = ax.imshow(data)
ax.set_ylim((0, 15000))

for i in range(frames):
    t0=time.time()
    l1.set_data(*random_data(datasize))
    ax.set_title("Frame: "+str(i+1))
    #for images:
    #im.set_cdata(new_data)
    fig.savefig(os.path.join(outputdir,
                random_prefix+'img'+str(i).zfill(4)+'.png'), format='png', dpi=150)
    #gc.collect()
    print("Frame "+str(i)+"/"+str(frames)+", "+
          ('%.3g'%(time.time()-t0)+" per frame"))

os.system("cd "+outputdir+" && "+
          "ffmpeg -r "+fps+" -i "+random_prefix+"img%04d.png "+
          "-c:v libx264 -r "+fps+" -pix_fmt yuv420p output.mp4 -y "+
          "&& rm "+random_prefix+"*.png")
#make a gif (optional)
os.system("cd "+outputdir+" && "+
          """ffmpeg -i output.mp4 -vf "fps="""+fps+""",scale=640:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif""")
