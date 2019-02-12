import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.3

komoka = [15, 14, 23]
oxbow = [10, 18, 12]
dingman = [13, 15, 14]

komokabars = np.arange(len(komoka))
oxbowbars = [x + barWidth for x in komokabars]
dingmanbars = [x + barWidth for x in oxbowbars]

plt.bar(komokabars, komoka, color='#FF0000', width = barWidth, edgecolor = 'white', label = 'Komoka')
plt.bar(oxbowbars, oxbow, color='#00FF00', width = barWidth, edgecolor = 'white', label = 'Oxbow')
plt.bar(dingmanbars, dingman, color='#0000FF', width = barWidth, edgecolor = 'white', label = 'Dingman')

plt.xlabel('Fishes Caught From 2016 to 2018', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(komoka))], ['2016', '2017', '2018'])

plt.legend()
plt.show()