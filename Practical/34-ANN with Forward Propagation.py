import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

X, y = load_iris(return_X_y=True)
y = OneHotEncoder(sparse_output=False).fit_transform(y.reshape(-1,1))
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = Sequential([
    Dense(10, activation='relu', input_dim=4),
    Dense(3, activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=50, verbose=0)
print("Accuracy:", model.evaluate(X_test, y_test, verbose=0)[1])
