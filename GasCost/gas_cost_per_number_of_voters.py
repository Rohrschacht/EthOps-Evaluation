#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

C_constant = 65120
C_voter = 8046

x = np.arange(0, 21, 1)
y = C_constant + C_voter * x

plt.plot(x, y)
# plt.title('Gas cost per number of voters')
plt.xticks(x)
plt.ylim(ymin=0)
plt.xlim(xmin=0, xmax=x[-1])
plt.yticks(np.linspace(0, y[-1], 20))
plt.xlabel('Number of voters')
plt.ylabel('Gas cost')

plt.savefig('gas_cost_per_number_of_voters.png', bbox_inches='tight')

