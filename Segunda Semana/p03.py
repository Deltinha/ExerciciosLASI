from sklearn import neighbors
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import normalize
import seaborn as sns
import pandas as pd

creditData = pd.read_csv('german_credit_data.csv', sep = ';')

target_names = teste2 = creditData.iloc[:,2:].values.ravel()

creditData.replace(to_replace='good', value=1, inplace=True)
creditData.replace(to_replace='bad', value=0, inplace=True)

n_neighbors = 5
weights = 'uniform'

input_X = creditData.iloc[:,:2].values
X = normalize(input_X, axis=0, norm='max')

y = creditData.iloc[:,2:].values.ravel()

h = .02

cmap_light = ListedColormap(['moccasin', 'cornflowerblue'])
cmap_bold = ['darkorange', 'darkblue']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 42)

clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
clf.fit(X_train,y_train)

print(accuracy_score(y_test, clf.predict(X_test)))

plt.figure(figsize=(10, 8))

sns.scatterplot(x=X[:,0], y=X[:,1], hue=(target_names),
                palette=(cmap_bold), edgecolor='k')
plt.xlabel('Age')
plt.ylabel('Credit amount')
plt.show()