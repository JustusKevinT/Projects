
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

(X_train, y_train) , (X_test, y_test) = keras.datasets.mnist.load_data()
len(X_train), len(X_test)
X_train[0].shape
X_train[0]
plt.matshow(X_train[0])
plt.matshow(X_train[1])
plt.matshow(X_train[2])
y_train[0], y_train[1], y_train[2]
y_train[:5]
X_train.shape
X_train, X_test = X_train/255, X_test/255
X_train_flattened = X_train.reshape(len(X_train), 28*28)
X_test_flattened = X_test.reshape(len(X_test), 28*28)
X_train_flattened
X_test_flattened
X_train_flattened.shape
X_test_flattened.shape
X_test_flattened[0]
model = keras.Sequential([
    keras.layers.Dense(100, input_shape=(784,), activation="relu"),
    keras.layers.Dense(10, activation = "sigmoid")
])
model.compile(
    optimizer="adam",
    loss = "sparse_categorical_crossentropy",
    metrics = ["accuracy"]
)
model.fit(X_train_flattened, y_train, epochs = 50)
model.evaluate(X_test_flattened, y_test)
plt.matshow(X_test[0])
model.predict(X_test_flattened)
temp_res = model.predict(X_test_flattened)
temp_res[0]
np.argmax(temp_res[0])
plt.matshow(X_test[1])
temp_res = model.predict(X_test_flattened)
temp_res[1]
np.argmax(temp_res[1])
temp_res_labels = [np.argmax(i) for i in temp_res]
temp_res_labels[:5]
ConfusionMatrix = tf.math.confusion_matrix(labels = y_test, predictions = temp_res_labels)
ConfusionMatrix
plt.figure(figsize = (10,8))
sn.heatmap(ConfusionMatrix, annot = True, fmt="d")
plt.xlabel("Predicted")
plt.ylabel("Original")
