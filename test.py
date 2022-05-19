import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("./data/student-mat.csv",sep=";")
plt.hist(df['absences'])

plt.xlabel('absences')
plt.ylabel('count')

plt.grid(True)
plt.show()