import pandas as pd
from matplotlib import pyplot as plt
# This is a simple code in order to get familiar with the data analysis and graphing in python
# Note this code will not work on its own you need to instal modules
x = [1,2,3]
y = [1,4,9]
z = [10, 5 ,0]
plt.plot(x,y)
plt.plot(x,z)
plt.title("Test plot")
plt.xlabel("X")
plt.ylabel("Y and z")
## you can also add a legend
plt.legend(["this is y", "this is z"])
## you can import CV files
sample_data = pd.read_csv('sample_data.csv')
type(sample_data)
plt.show()