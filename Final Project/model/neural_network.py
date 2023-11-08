# neural_network.py
# This file defines the neural network model and the training process.

from tensorflow import keras
from sklearn.metrics import r2_score, mean_squared_error
from keras.callbacks import EarlyStopping

class NeuralNetworkModel:
    def __init__(self, input_shape, dense1_units=64, dense2_units=32, learning_rate=0.001):
        # Define the model with variable layer units and activation function
        self.model = keras.Sequential([
            keras.layers.Dense(dense1_units, activation='relu', input_shape=input_shape),
            keras.layers.Dense(dense2_units, activation='relu'),
            keras.layers.Dense(1)  # One output: reliability
        ])

        # Adam optimizer with variable learning rate
        optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
        self.model.compile(loss='mean_squared_error', optimizer=optimizer)

    def train(self, X_train, y_train, validation_split=0.07, epochs=1000, batch_size=77, min_delta=0.00001, patience=100):
        # Define early stopping with variable min_delta and patience
        early_stopping = EarlyStopping(
            min_delta=min_delta,  
            patience=patience,  
            restore_best_weights=True
        )

        # Train the model with early stopping and variable parameters
        history = self.model.fit(
            X_train, y_train,
            validation_split=validation_split,
            epochs=epochs,
            batch_size=batch_size,
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
