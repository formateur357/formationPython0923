import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/morganguy/Formation_Workspace/formationPython0923/exemples/ventes.csv")
# print(str(data.describe()))
# data.head()
# data.info()
# data.describe()

plt.figure(figsize=(10, 6))
plt.bar(data['Mois'], data['Chiffre d\'affaires'])
plt.xlabel('Mois')
plt.ylabel('Chiffre d\'affaires en dollars')
plt.title('Evolution du chiffre d\'affaires par mois')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()