import numpy as np
import	matplotlib.pyplot as plt

members = [52, 48, 67, 45, 45, 50, 55, 67, 65, 70, 60, 60, 55, 60, 65, 75, 80]
years = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
y_pos = np.arange(len(years))

plt.bar(y_pos, members, width=0.5)

plt.xticks(y_pos, years, fontsize=8, rotation='90')
plt.xlabel('Year')
plt.ylabel('Number of Members')

plt.title('Number of Members of the TRAA from 2002 to 2018')

plt.show()