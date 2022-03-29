from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from pathlib import Path
dir_str_mod_wsb = './wsb_mod_percent/'

pathlist_mod = Path(dir_str_mod_wsb).glob('**/*.csv')

accuracies = {}


def mlp():
    for path in pathlist_mod:
        data = pd.read_csv(path)

        # Spliting data into Feature and
        X = data[['Sentiment']]
        X = X.astype('double')
        y = data[['High']]
        y = y.astype('double')

        # Import train_test_split function

        # Split dataset into training set and test set
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42)  # 70% training and 30% test
        clf = MLPClassifier(hidden_layer_sizes=(6, 5),
                            random_state=5,
                            verbose=True,
                            learning_rate_init=0.01)

        # Fit data onto the model
        clf.fit(X_train.values.ravel().reshape(1, -1),
                y_train.values.ravel().reshape(1, -1))

        ypred = clf.predict(X_test)

        accuracies[data["Ticker"]] = accuracy_score(y_test, ypred)


mlp()
