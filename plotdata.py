import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

nodes = [25,50,75,100,125,150,175,200]

graphToolSeries = pd.Series([1.9077062606811523,8.724808692932129,15.401887893676758,37.48791217803955,45.72787284851074,59.198594093322754,163.35787773132324,151.52406692504883,], index = nodes)
tGraphSeries = pd.Series([0.051021575927734375,0.46660900115966797,1.6940593719482422,5.517888069152832,11.269521713256836,21.17624282836914,75.85642337799072,86.13100051879883], index = nodes)

df = pd.DataFrame({"T Graph":tGraphSeries,"Graph Tool":graphToolSeries})

ax = df.plot.bar(color=["mediumseagreen","tomato"], rot=0, title="Graph Tool vs T Graph Performance for Finding Shortest DAG Paths")

ax.set_xlabel("Number of Nodes")
ax.set_ylabel("Runtime (ms)")

plt.show()

ser = pd.Series(np.random.normal(size=100))
print(ser)
ser = ser.sort_values()
ser[len(ser)] = ser.iloc[-1]
cum_dist = np.linspace(0.,1.,len(ser))
ser_cdf = pd.Series(cum_dist, index=ser)
ser_cdf.plot(drawstyle='steps')

plt.show()