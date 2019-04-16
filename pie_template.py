import matplotlib.pyplot as plt
from math import floor
import pathlib

data   = list()
labels = list()
colors = list()
title  = ''
source = ''
filename = pathlib.Path(__file__)

font       = 'Serif'
rotation   = False
background = '#111111'
title_txt  = 'cyan'
sub_text   = 'royalblue'
minor_txt  = 'darkcyan'

###############################################################################

plt.pie(data, labels=labels, colors=colors, 
        textprops={'fontname': font, 'fontsize': 9, 'color': sub_text},
        autopct=lambda n: str(floor(n))+'%', rotatelabels=rotation)

plt.suptitle(title, fontname=font, fontsize=14, color=title_txt)
plt.title(source, fontname=font, fontsize=8, color=minor_txt)

plt.gcf().set_size_inches(6, 6)
plt.axes().figure.set_facecolor(background)

plt.savefig(filename.with_suffix('.jpg'), 
        facecolor=plt.axes().figure.get_facecolor())

plt.show()
