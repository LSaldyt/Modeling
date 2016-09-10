import matplotlib.pyplot as plt

def graph(datasets=[], colors=[]):
    if len(colors) < len(datasets):
        colors = colors + [None] * (len(datasets) - len(colors))

    for dataset, color in zip(datasets, colors):
        if color is None:
            plt.plot(dataset)
        else:
            plt.plot(dataset, c=color)

    plt.show()
