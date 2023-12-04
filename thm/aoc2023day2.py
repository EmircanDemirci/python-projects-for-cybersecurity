import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.rcParams["figure.figsize"] = [7.00,3.50]
plt.rcParams["figure.autolayout"] = True

columns = ["PacketNumber","Timestamp","Source" , "Destination" , "Protocol"]
df = pd.read_csv("network_traffic.csv" , usecols = columns)
print("Contents in csv file" , df)

print(sorted(list(Counter(df.Source).items()) , key = lambda x: x[1]))#What IP address sent the most amount of traffic during the packet capture?


print("\n",sorted(list(Counter(df.Protocol).items()) , key = lambda x: x[1]))#What was the most frequent protocol?
