
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

input_data = pd.read_csv("D:/College/interview-projects/PYTHONR-INTERNSHIP/Psyliq intern solutions/titanic_train.csv")

input_data.head()

input_data.shape

input_data.info()

input_data.isnull().sum()

input_data = input_data.drop(columns="Cabin", axis=1)

input_data["Age"].fillna(input_data["Age"].mean(), inplace = True)

input_data["Embarked"].fillna(input_data["Embarked"].mode()[0], inplace = True)

input_data.isnull().sum()

input_data.describe()

input_data["Survived"].value_counts()

sns.set()

sns.countplot(x= "Survived",hue = "Survived", data = input_data, palette = "Set1", legend = False)

input_data["Sex"].value_counts()

sns.countplot(x= "Sex",hue = "Sex", data = input_data, palette = "Set1", legend = False)

sns.countplot(x= "Sex",hue = "Survived", data = input_data, palette = "Set1")

sns.countplot(x= "Pclass",hue = "Pclass", data = input_data, palette = "Set1", legend = False)

sns.countplot(x= "Pclass",hue = "Survived", data = input_data, palette = "Set1")

input_data["Embarked"].value_counts()

input_data["Sex"].value_counts()

input_data.replace({'Sex': {"male": 0, "female": 1}, 'Embarked': {"S": 0, "C": 1, "Q": 2}}, inplace=True)

input_data.head()

X,Y = input_data.drop(columns = ["PassengerId","Name","Ticket", "Survived"], axis = 1), input_data["Survived"]

X

Y

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 2)

print(X.shape, X_train.shape, X_test.shape)

model = LogisticRegression( max_iter=1000)

model.fit(X_train, Y_train)

X_train_prediction = model.predict(X_train)

print(X_train_prediction)

train_data_accuracy = accuracy_score(Y_train,X_train_prediction)
print(train_data_accuracy)

X_test_prediction = model.predict(X_test)

print(X_test_prediction)

test_data_accuracy = accuracy_score(Y_test,X_test_prediction)
print(test_data_accuracy)

