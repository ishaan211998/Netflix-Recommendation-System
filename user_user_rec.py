import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

data1 = pd.read_csv("./../netflix-prize-data/updated_data1.txt", sep = ",")
#data2 = pd.read_csv("./../netflix-prize-data/combined_data_2.txt", sep = ",")
#data3 = pd.read_csv("./../netflix-prize-data/combined_data_3.txt", sep = ",")
#data1.columns = ["ALL"]
print(data1)

#for index, row in data1.iterrows():
#    print(type(row["ALL"]))

#print(data2)
#print(data3)
