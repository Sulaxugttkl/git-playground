import time
from matplotlib.animation import FuncAnimation
import numpy as np

import matplotlib.pyplot as plt

start_time = time.time()
counter = 0
times = []
counters = []

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlabel('Elapsed Time (s)')
ax.set_ylabel('Counter')
ax.set_title('Counter Over Time')

def update(frame):
    global counter, start_time, times, counters
    elapsed = time.time() - start_time
    print(f"Counter: {counter}, Elapsed: {elapsed:.2f}s")
    
    times.append(elapsed)
    counters.append(counter)
    counter += 1
    
    line.set_data(times, counters)
    ax.set_xlim(0, max(elapsed + 1, 10))
    ax.set_ylim(0, max(counter + 5, 10))
    
    return line,

try:
    ani = FuncAnimation(fig, update, interval=1000, blit=True)
    plt.show()
except KeyboardInterrupt:
    print("\nStopped by user")
