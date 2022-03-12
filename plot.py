import matplotlib.pyplot as plt

def do_plot(data, series):
    fig, ax1 = plt.subplots()

    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Voltage (V)", color='b')
    ax1.plot(data.time, data.voltage, color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    ax2 = ax1.twinx()

    ax2.set_ylabel("Current (A)", color='r')
    ax2.plot(data.time, data.current, color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    plt.savefig('plots\\plot' + series + '.png')