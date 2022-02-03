import pandas as pd
from pandas.core import indexing

frame = pd.read_csv("dataset/covid-19-vaccination-stance-3249.csv")
id = frame["id"][:-1]
with open("twitter_ids.txt", 'w') as ofile:
    for i in range(len(indexing)):
        ofile.write(str(id[i]))
        ofile.write('\n')





