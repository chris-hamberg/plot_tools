import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pathlib


#NOTE Plot Info Configuration
font     = 'Serif'
title    = ''
source   = 'Source: '
ylabel   = ''
filename = pathlib.Path(__file__).with_suffix('.jpg')


#NOTE Data Configuration
data       = None
categories = None
positions  = np.arange(len(categories))


# NOTE Color Configuration
background = 'white'
spines     = 'black'
special    = spines # Bottom and left spines
# --- text colors
bold       = 'black'
trim       = 'darkgrey'
# --- bar colors
bars       = 'red'
edges      = 'black'
width      = 1
# --- grid colors
grid       = 'white'
alpha      = 0.1


#NOTE Geometry Configuration
x_rotation = 0
x_size     = 7
y_size     = 6
y_ticks    = True
x_ticks    = False


################################################################## Make the plot
plt.gcf().set_size_inches(x_size, y_size)
plt.bar(positions, data, align='center', color=bars, 
        edgecolor=edges, linewidth=width)
plt.xticks(positions, categories, fontsize=10, fontname=font, 
        rotation=x_rotation, color=bold)
plt.ylabel(ylabel, fontsize=10, fontname=font, 
        color=bold)
plt.yticks(color=trim)
plt.suptitle(title, fontsize=14, fontname=font, color=bold)
#plt.title(source, fontsize=8, fontname=font, color=trim)
plt.figtext(.5, 0.01, source, wrap=True, ha='center', fontname=font, fontsize=8,
        color=trim)
plt.grid(color=grid, alpha=alpha)

 
ax = plt.axes()
ax.patch.set_facecolor(background)
ax.figure.set_facecolor(background)
ax.set_axisbelow(True)
for position in ['top', 'right']:
    ax.spines[position].set_color(spines)
for position in ['bottom', 'left']:
    ax.spines[position].set_color(special)
ax.tick_params(top=False, bottom=False, left=y_ticks, right=x_ticks, 
        labelleft=True, labelbottom=True)


plt.savefig(filename, facecolor=ax.figure.get_facecolor())
plt.show()
