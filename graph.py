import matplotlib.pyplot as plt

def graph(xs, ys, extra=[]):
    plt.plot(xs)
    plt.plot(ys)
    for ys in extra:
        plt.plot(ys)
    plt.ylabel('some numbers')
    plt.show()
