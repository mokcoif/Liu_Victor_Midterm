import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.25

rainbowTroutEggs = [100000, 150000, 100000, 50000, 150000]
rainbowTroutHatched = [80000, 120000, 90000, 40000, 140000]
brownTroutEggs = [100000, 80000, 70000, 80000, 100000]
brownTroutHatched = [70000, 70000, 70000, 70000, 90000]

r1 = np.arange(lens(rainbowTroutEggs))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

plt.bar(r1, rainbowTroutEggs, color='#d4af37', width=barWidth, edgecolor='white', label='Total Rainbow Trout Eggs')
plt.bar(r2, rainbowTroutHatched, color='#c49f27', width=barWidth, edgecolor='white', label='Rainbow Trout Eggs that Hatched')
plt.bar(r3, brownTroutEggs, color='#a52a2a', width=barWidth, edgecolor='white', label='Total Brown Trout Eggs')
plt.bar(r4, brownTroutHatched, color='#d2691e', width=barWidth, edgecolor='white', label='Brown Trout Eggs that Hatched')

plt.xlabel('Eggs Received and Hatched from 2014 to 2018', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(rainbowTroutEggs))], ['2014', '2015', '2016', '2017', '2018'])

plt.legend()
plt.show()