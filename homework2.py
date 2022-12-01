import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

March92021 = pd.read_csv("March92021.csv", dayfirst=True, sep=",",
                         header=0, decimal=b".", index_col=0,
                         parse_dates=[[0, 1, 2, 3]], usecols=[0, 1, 2, 3, 5])

March92021.info()

# Day1
fig, ax = plt.subplots(1, figsize=(20, 5))
plt.plot(March92021, color='orange', marker=" ",
         markersize=3, linestyle='-', linewidth=1)
plt.title('2022-03-09', fontsize=20, fontweight="bold")
plt.ylabel("Direct solar radiation [W/m2]", fontweight='bold')
plt.grid(True)
plt.tight_layout()
xfmt = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.show()


July92021 = pd.read_csv("July92021.csv", dayfirst=True, sep=",",
                        header=0, decimal=b".", index_col=0,
                        parse_dates=[[0, 1, 2, 3]], usecols=[0, 1, 2, 3, 5])

July92021.info()


# Day2
fig, ax = plt.subplots(1, figsize=(20, 5))
plt.plot(July92021, color='red', marker=" ",
         markersize=3, linestyle='-', linewidth=1)
plt.title('2022-07-09', fontsize=20, fontweight="bold")
plt.ylabel("Direct solar radiation [W/m2]", fontweight='bold')
plt.grid(True)
plt.tight_layout()
xfmt = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.show()

December92021 = pd.read_csv("December92021.csv", dayfirst=True, sep=",",
                            header=0, decimal=b".", index_col=0,
                            parse_dates=[[0, 1, 2, 3]], usecols=[0, 1, 2, 3, 5])

December92021.info()


# Day3
fig, ax = plt.subplots(1, figsize=(20, 5))
plt.plot(December92021, color='blue', marker=" ",
         markersize=3, linestyle='-', linewidth=1)
plt.title('2022-12-09', fontsize=20, fontweight="bold")
plt.ylabel("Direct solar radiation [W/m2]", fontweight='bold')
plt.grid(True)
plt.tight_layout()
xfmt = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.show()
