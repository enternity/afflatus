import numpy as np
from matplotlib import pyplot as plt

def generate_plot(platforms, output_file):
    """Generates a bar chart out of the given platforms and writes the output
    into the specified file as PNG image.

    """
    # First off we need to convert the platforms in a format that can be
    # attached to the 2 axis of our bar chart. "labels" will become the
    # x-axis and "values" the value of each label on the y-axis:
    labels = []
    values = []
    for platform in platforms:
        name = platform['name']
        adjusted_price = platform['adjusted_price']
        price = platform['original_price']

        # Skip prices higher than 2000 USD simply because it would make the
        # output unusable.
        if price > 2000:
            continue

        # If the name of the platform is too long, replace it with the
        # abbreviation. list.insert(0, val) inserts val at the beginning of
        # the list.
        if len(name) > 15:
            name = platform['abbreviation']
        labels.insert(0, u"{0}\n$ {1}\n$ {2}".format(name, price,
                                                     round(adjusted_price, 2)))
        values.insert(0, adjusted_price)

    # Let's define the width of each bar and the size of the resulting graph.
    width = 0.3
    ind = np.arange(len(values))
    fig = plt.figure(figsize=(len(labels) * 1.8, 10))

    # Generate a subplot and put our values onto it.
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(ind, values, width, align='center')

    # Format the X and Y axis labels. Also set the ticks on the x-axis slightly
    # farther apart and give then a slight tilting effect.
    plt.ylabel('Adjusted price')
    plt.xlabel('Year / Console')
    ax.set_xticks(ind + 0.3)
    ax.set_xticklabels(labels)
    fig.autofmt_xdate()
    plt.grid(True)

    plt.savefig(output_file, dpi=72)