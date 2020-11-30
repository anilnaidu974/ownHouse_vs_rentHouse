import os
import pandas as pd
import numpy as np
import cv2
from tqdm import tqdm
import pickle

from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import pickle
from keras.utils import to_categorical

dataset = pd.read_csv('own_vs_rent.csv')

new_df = dataset.copy()
new_df['aaset_type'] = new_df['Own_House_Asset'] - new_df['Rent_House_Asset']
new_df['aaset_type'] = new_df['aaset_type'].apply(lambda x : 1 if x>0 else 0)
features = new_df.drop(labels = ['Own_House_Asset','Rent_House_Asset','aaset_type'], axis=1)
labels = new_df['aaset_type']

X = np.array(features)
y = np.array(labels)

(trainX, testX, trainY, testY) = train_test_split(X,y, test_size=0.25, random_state=42)

trainY_cat = to_categorical(trainY)
testY_cat = to_categorical(testY)

x_scaler = StandardScaler()
trainX_new = x_scaler.fit_transform(trainX)
testX_new = x_scaler.transform(testX)


xgb.fit(trainX_new,trainY)

# make predictions for test data
y_pred = xgb.predict(testX_new)
predictions = [round(value) for value in y_pred]

xgb_file = "xgb_cls.pkl"
x_scaler_file = "x_scaler.pkl"

# save
pickle.dump(xgb, open(xgb_file, "wb"))
# load
# xgb = pickle.load(open("xgb_cls.pkl", "rb"))

# save
pickle.dump(x_scaler, open(x_scaler_file, "wb"))