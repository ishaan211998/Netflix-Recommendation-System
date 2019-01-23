import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

data1 = pd.read_csv("./../netflix-prize-data/updated_data1.txt", sep = ",", header = None)
data1.columns = ["UserID", "Ratings", "Date", "MovieID"]
#print(data1)

Mean = data1.groupby(["UserID"], as_index = False, sort = False).mean().rename(columns = {"Ratings": "rating_mean"})[["UserID", "rating_mean"]]
data1 = pd.merge(data1, Mean, on = "UserID", how = "left", sort = False)
data1["Adjusted_Ratings"] = data1["Ratings"] - data1["rating_mean"]
#print(data1)

distinct_users = np.unique(data1["UserID"]).size
print(distinct_users)
