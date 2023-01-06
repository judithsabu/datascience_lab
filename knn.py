import pandas as pd
dataset=pd.read_csv("iris.csv")
X=dataset.iloc[:,:1].values
Y=dataset.iloc[:4].values
print(X)
print(Y)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20)
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train,Y_train)
Y_pred=classifier.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(Y_train,Y_pred))