from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score
from pathlib import Path
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

dir_str_mod_wsb = './wsb_mod_percent/'

pathlist_mod = Path(dir_str_mod_wsb).glob('**/*.csv')

accuracies = {}


def mlp():
    i = 0
    for path in pathlist_mod:
        if(i == 1):
            break

        filename = pd.read_csv(path)
        data = filename[["High"]]
        data = data.rename(columns={"High": "Actual_High"})
        data["Target"] = filename.rolling(2).apply(
            lambda x: x.iloc[1] > x.iloc[0])["High"]

        data_prev = filename.copy()  # vet inte riktigt varför hehhe
        data_prev = data_prev.shift(1)
        predictors = ["Normalized_Sentiment"]
        data = data.join(data_prev[predictors]).iloc[1:]

        print(data.head(100))

        # Create a random forest classification model.  Set min_samples_split high to ensure we don't overfit.
        model = Sequential()
        model.add(LSTM(50, return_sequences=True))
        model.add(LSTM(50, return_sequences=True))
        model.add(LSTM(50))
        model.add(Dense(1))
        model.compile(loss='mean_squared_error', optimizer='adam')

        # Create a train and test set
        x = np.array(data["Normalized_Sentiment"])
        y = np.array(data["Target"])
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.18, random_state=0)
        print(x_train.shape)
        print(y_train.shape)
        print(x_train.reshape(1, -1).tolist())

        model.fit(x_train.reshape(1, -1).tolist(),
                  y_train.reshape(1, -1).tolist())
        i += 1


mlp()
