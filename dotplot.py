# REF: https://stackoverflow.com/questions/49703938/how-to-create-a-dot-plot-in-matplotlib-not-a-scatter-plot
# NOTE make a dotplot
import matplotlib.pyplot as plt

def dotplot(xs, ys, color='red', size=10, edgecolor='black', edgewidth=1):
    for x, y in zip(xs, ys): 
        plt.plot([x]*y, list(range(y)), 'o', color=color, markersize=size, 
                markeredgecolor=edgecolor, markeredgewidth=edgewidth) 
    return plt
