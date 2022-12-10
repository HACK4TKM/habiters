import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
data = pd.read_excel('sampledata.xls')
data.plot()
plt.show()