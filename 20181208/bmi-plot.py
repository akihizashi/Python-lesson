import matplotlib.pyplot as plt
import pandas as pd
import os

csv_dir = os.path.dirname(os.path.abspath(__name__))
csv_path = os.path.join(csv_dir, '/csv/bmi_1000.csv')

tbl = pd.read_csv(csv_path, index_col=2)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def scatter(label, color):
    b = tbl.loc[label]
    ax.scatter(b["weight"], b["height"], c=color, label = label)

scatter("fat", "red")
scatter("normal", "yellow")
scatter("thin", "purple")

ax.legend()
#plt.savefig("bmi-test-100.png")
plt.show()
