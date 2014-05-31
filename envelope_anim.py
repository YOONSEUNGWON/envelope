# Animation using generator in FuncAnimation

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

# Define constants
VERSION = 2

if VERSION == 2:
    # plt.axes(xlim=(-x_Bound, x_Bound), ylim=(y_Lower, y_Upper))
    x_Bound = 35
    y_Lower, y_Upper = -100, 200

    # x = np.array([x_Min, x_Max])
    x_Max = 50
    x_Min = -x_Max

    # t = -t_max, -t_max + 1, ..., t_max
    t_Max = 20
    Interval_ms = 80

if VERSION == 3:
    # plt.axes(xlim=(-x_Bound, x_Bound), ylim=(y_Lower, y_Upper))
    x_Bound = 50
    y_Lower, y_Upper = -100, 600

    # x = np.array([x_Min, x_Max])
    x_Max = 50
    x_Min = -x_Max

    # t = -t_max, -t_max + 1, ..., t_max
    t_Max = 60
    Interval_ms = 50

else:
    VERSION = 1
    # plt.axes(xlim=(-x_Bound, x_Bound), ylim=(y_Lower, y_Upper))
    x_Bound = 35
    y_Lower, y_Upper = -100, 200

    # x = np.array([x_Min, x_Max])
    x_Max = 50
    x_Min = -x_Max

    # t = -t_max, -t_max + 1, ..., t_max
    t_Max = 22
    Interval_ms = 100


fig = plt.figure()
ax = plt.axes(xlim=(-x_Bound, x_Bound), ylim=(y_Lower, y_Upper))
ax.axhline(linewidth=2.0, color="black")
ax.axvline(linewidth=2.0, color="black")
fig.suptitle('Envelope Theorem.ver' + str(VERSION), fontsize=20)
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
ax.grid()
line, = ax.plot([], [], 'r-', lw=4)


def f():
    line.set_data([], [])
    return line,


# http://matplotlib.org/examples/animation/animate_decay.html
def t_gen():
    t = -t_Max
    while t <= t_Max:
        yield t
        t += 1


def animate(t):
    x = np.array([x_Min, x_Max])  # Two points are enough to determine a line
    y = t*x - t**2
    ax.plot(x, y, 'b-')
    line.set_data(x, y)
    return line


anim = animation.FuncAnimation(fig, animate, t_gen, init_func=f,
                               interval=Interval_ms, blit=False, repeat=False)

plt.show()
