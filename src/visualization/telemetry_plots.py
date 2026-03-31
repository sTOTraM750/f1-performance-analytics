import matplotlib.pyplot as plt
import matplotlib.animation as animation


def plot_speed(trace):
    plt.figure()
    plt.plot(trace['Distance'], trace['Speed'])
    plt.title("Speed vs Distance")
    plt.xlabel("Distance")
    plt.ylabel("Speed")
    plt.show()


def plot_throttle(trace):
    plt.figure()
    plt.plot(trace['Distance'], trace['Throttle'])
    plt.title("Throttle Application")
    plt.xlabel("Distance")
    plt.ylabel("Throttle")
    plt.show()

def plot_track(trace):
    plt.figure(figsize=(6,6))
    plt.plot(trace['X'], trace['Y'])
    plt.title("Track Map")
    plt.axis('equal')
    plt.show()

def plot_speed_track(trace):
    plt.figure(figsize=(6,6))
    sc = plt.scatter(trace['X'], trace['Y'], c=trace['Speed'], cmap='coolwarm', s=5)
    plt.colorbar(sc, label="Speed")
    plt.title("Speed Heatmap on Track")
    plt.axis('equal')
    plt.show()

def animate_lap(trace):
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)

    def update(i):
        line.set_data(trace['X'][:i], trace['Y'][:i])
        return line,

    ani = animation.FuncAnimation(fig, update, frames=len(trace), interval=50)
    plt.show()