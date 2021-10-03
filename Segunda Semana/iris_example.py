import numpy as np
from sklearn import neighbors, datasets
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns

n_neighbors = 15
weights = 'uniform'

iris = datasets.load_iris()

X = iris.data[:, :2]
y = iris.target

h = .02

cmap_light = ListedColormap(['moccasin', 'cornflowerblue','pink'])
cmap_bold = ['darkorange', 'darkblue','crimson']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 42)

clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
clf.fit(X_train,y_train)

print(accuracy_score(y_test, clf.predict(X_test)))

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

Z = Z.reshape(xx.shape)
plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, Z, cmap=cmap_light)

sns.scatterplot(x=X[:,0], y=X[:,1], hue=(iris.target_names[y]),
                palette=(cmap_bold), edgecolor='k')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()