import pandas as pd
import numpy as np

def logistic_regression(data, labels, weights, num_epochs, learning_rate):
    X = np.c_[np.ones(len(data)), data]
    X_t = X.T
    for epoch in range(num_epochs):
        dot_item = -np.dot(X, weights)
        temp = labels - 1/(1+np.exp(dot_item))
        for i in range(len(weights)):
            weights[i] += np.dot(learning_rate, np.dot(X_t[i], temp))
    return weights
