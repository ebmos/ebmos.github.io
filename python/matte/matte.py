import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("ssbmedier.csv", index_col = 0, skiprows = (0, 1), \
    sep =";", na_values=[".", ".."], encoding = "latin-1")

K = []   # Lager en tom liste K 
startVerdi = 2010   # Lager variabel for det første årstallet
for i in range(0, 10):
    K.append(startVerdi + i)
data.columns = K  # Setter radoverskriftene i variabelen data lik innholdet av lista K 

data = data.transpose()
data.plot().legend(bbox_to_anchor = (1, 1))

plt.show()
print(data)
print(data.describe())