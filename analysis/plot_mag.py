#!/user/bin/env python3
from load_to_df import LoadLarus2Df
import numpy as np
import matplotlib.pyplot as plt
import sys

# Howto execute:
# python3 plot_wind.py ../flightdata/230414_085440.f37.f110
file = sys.argv[1]
data = LoadLarus2Df(file)
df = data.df

# Prepare the data
t = df.index / 100.0 / 60.0   # 100Hz ticks to minutes for the time axis
nav_ind_abs = np.sqrt(np.square(df['nav ind mag N']) + np.square(df['nav ind mag E']) + np.square(df['nav ind mag D']))

# Plot the data
figure, axis = plt.subplots()
figure.suptitle("Induction in earth system: " + file)
plt.autoscale(enable=True, axis='y')
axis.grid()
axis.set_xlabel('t [minutes]')

axis.plot(t, nav_ind_abs, "k", linewidth=1)
axis.legend(["nav ind abs"], loc="lower left")
par1 = axis.twinx()
par1.plot(t, df['nav ind mag N'], "r-", linewidth=0.5)
par1.plot(t, df['nav ind mag E'], "g-", linewidth=0.5)
par1.plot(t, df['nav ind mag D'], "b-", linewidth=0.5)

minimum = df['nav ind mag N'].min()
maximum = df['nav ind mag N'].max()
if df['nav ind mag E'].min() < minimum:
    minimum = df['nav ind mag E'].min()
if df['nav ind mag E'].max() > maximum:
    maximum = df['nav ind mag E'].max()
if df['nav ind mag D'].min() < minimum:
    minimum = df['nav ind mag D'].min()
if df['nav ind mag D'].max() > maximum:
    maximum = df['nav ind mag D'].max()
par1.set_ylim(minimum - 0.5, maximum + 1.5)
par1.legend(['nav ind mag N', 'nav ind mag E', 'nav ind mag D'], loc="lower right")

figure, axis = plt.subplots()
figure.suptitle("Raw magnetic sensor values: " + file)
plt.autoscale(enable=True, axis='y')
axis.grid()
axis.set_xlabel('t [minutes]')

axis.plot(t, df['mag x'], "r-", linewidth=0.5)
axis.plot(t, df['mag y'], "g-", linewidth=0.5)
axis.plot(t, df['mag z'], "b-", linewidth=0.5)
axis.legend(['mag x', 'mag y', 'mag z'], loc="lower right")
plt.show()



