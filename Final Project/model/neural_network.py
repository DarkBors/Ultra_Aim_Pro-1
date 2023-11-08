# neural_network.py
# This file defines the neural network model and the training process.

from tensorflow import keras
from sklearn.metrics import r2_score, mean_squared_error
from keras.callbacks import EarlyStopping

class NeuralNetworkModel:
    def __init__(self, input_shape):
        # Define the model with reduced complexity
        self.model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=input_shape),
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(1)  # One output: reliability
        ])

        # Adam optimizer with lower learning rate Default learning_rate=0.001
        optimizer = keras.optimizers.Adam(learning_rate=0.001)
        self.model.compile(loss='mean_squared_error', optimizer=optimizer)

    def train(self, X_train, y_train):
        # Define early stopping
        early_stopping = EarlyStopping(
            min_delta=0.00001,  # minimum amount of change to count as an improvement
            patience=100,  # how many epochs to wait before stopping
            restore_best_weights=True
        )

        # Train the model with early stopping
        history = self.model.fit(
            X_train, y_train,
            validation_split=0.07,
            epochs=1000,
            batch_size=77,
            callbacks=[early_stopping]
        )
        return history

    def predict(self, X_test):
        # Make predictions
        return self.model.predict(X_test).flatten()

    def evaluate(self, X_test, y_test):
        # Calculate and print R^2 and MSE
        predicted_reliability = self.predict(X_test)
        r2 = r2_score(y_test, predicted_reliability)
        mse = mean_squared_error(y_test, predicted_reliability)
        return r2, mse
