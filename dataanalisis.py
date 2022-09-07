import inline as inline
import matplotlib as matplotlib
import pandas as pd
import numpy as np
#%matplotlib  inline
import matplotlib.pyplot as plt

icecream=pd.DataFrame([[1,464,10.6],[2,397,12.2],[3,493,14.9],[4,617,20.3],[5,890,25.2],[6,883,26.3],[7,1293,29.7],\
                      [8,1387,31.6],[9,843,27.7],[10,621,22.6],[11,459,15.5],[12,561,13.8]],\
                      columns=["month","months ice sell","avg Temp"])
#icecream["months ice sell "].plot()
#icecream["months ice sell"].plot(kind='bar')
#plt.show()
icecream[["months ice sell" , "avg Temp"]].plot(kind='bar' , colormap="Greys",edgecolor="k")

plt.title("2016 year ice selling in the world")
plt.xlabel("month")
plt.ylabel("months ice sell (yin)")
plt.show()