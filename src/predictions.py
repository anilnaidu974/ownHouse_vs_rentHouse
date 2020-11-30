import pandas as pd
import numpy as np 
import pickle


class predictionClass:

    def __init__(self):

        xgb_cls_file = open("./models/xgb_cls_50%.pkl",'rb')
        x_scaler_file = open("./models/x_scaler_50%.pkl",'rb')
        self.model = pickle.load(xgb_cls_file)
        self.x_scaler = pickle.load(x_scaler_file)

    def getPredictions(self,p_cost,loan,l_interest,years,rent,savings,s_interest,houseType):

        data = []
        data.append(int(p_cost))
        data.append(int(loan))
        data.append(float(l_interest))
        data.append(int(years))
        data.append(int(houseType))
        data.append(int(rent)+int(savings))
        data.append(float(s_interest)/100)

        if s_interest == 0:
            s_interest = 0.04  # normal bank interest

        data = np.array(data)
        data = self.x_scaler.transform(np.array([data]))
        predictions = self.model.predict(data)

        return predictions

        