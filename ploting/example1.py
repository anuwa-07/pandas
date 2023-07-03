import sys
import matplotlib
import pandas as pd
matplotlib.use('Agg')  # This is required to run matplotlib on a cluster
import matplotlib.pyplot as plt

df = pd.read_csv('./data/example1.csv')
df.plot()
plt.show()

# Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
