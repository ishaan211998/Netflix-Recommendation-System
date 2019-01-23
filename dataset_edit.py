import pandas as pd
import numpy as np

inp = -1

wr = open("./../netflix-prize-data/updated_data1.txt", "a+")

with open("./../netflix-prize-data/combined_data_1.txt") as f:
   for line in f:
       if "," in line:
           lst = line.split(" ")
           #print(lst)
           str1 = lst[0]
           str1 = str1[:-2]
           #print(str)
           #print(str1 +" "+str(inp) + "\n")
           wr.write(str1 +","+str(inp) + "\n")
       else:
           inp = int(line.split(":")[0])
           #print(inp)
