from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score

# load iris datasets
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

score = cross_val_score(knn, iris_X, iris_y, cv=5, scoring='accuracy')

print(score)
print(score.mean())
