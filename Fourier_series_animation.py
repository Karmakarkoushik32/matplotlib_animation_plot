# =====================================================================================================
N = 20

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

class revolver:
    def __init__ (self,center,theta, radius, time_interval,axis):
        self.center = center
        self.theta = theta
        self.radius = radius
        self.time_interval = time_interval
        self.line, = ax.plot([], [], marker = '.')
        
    def revolve(self,center=None):
        if center:
            self.center = center
        self.theta += self.time_interval
        self.x = self.center[0] + self.radius * np.cos(self.theta)
        self.y = self.center[1] + self.radius * np.sin(self.theta)
        self.line.set_data([self.x,self.center[0]], [self.y,self.center[1]])
        return self.line, (self.x,self.y)

def square_wave(n, time_interval):
    time = np.arange(0.01,(n/100)*2, 0.02) *time_interval
    redius = 1/np.arange(1,n*2,2)
    theta = np.full_like(fill_value=0, a=redius)
    return zip(time,redius,theta)

lim = 0
revolvers = []
for t,i,theta in square_wave(N,3):
    revolvers.append(revolver([0,0],theta, i, t ,ax))
    lim += i
    
ax.set_xlim(-lim*2, lim *6)
ax.set_ylim(-1.2, 1.2)

xdata, ydata =np.array([]), np.array([])
line_graph, = ax.plot([],[], c ='green') 
def update(frame):
    global xdata, ydata, j
    lines = []
    circles = []
    center = [0,0]
    for r in revolvers:
        line,center = r.revolve(center)
        lines.append(line)
    line_c, = ax.plot([center[0], lim],[center[1],center[1]],c='red',linestyle='dashed',marker='o') 
    
    if len(xdata) > 1500:
        xdata, ydata = xdata[ : -250], ydata[ : -250]
        
    xdata = np.insert(xdata, 0, lim) + 0.02
    ydata = np.insert(ydata, 0, center[1])
    
    line_graph.set_data(xdata, ydata)
    return *lines, *circles, line_c,line_graph,


animation = FuncAnimation(fig, update, blit=True, interval=1)
plt.title(f'Synthesizing a square wave function \nusing N={N} harmonics with Fourier analysis')
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticklabels([])
ax.set_yticks([])

plt.show()
