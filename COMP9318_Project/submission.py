import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
import math

## Project-Part1
def predict_COVID_part1(svm_model, train_df, train_labels_df, past_cases_interval, past_weather_interval, test_feature):
    x_train = pd.DataFrame(columns = ['day'], data= [i for i in range(31,len(train_df) + 1)])  #day 31 - 162
    y_train = train_labels_df.iloc[30:]                                        #day 31 - 162
    consider_features = ["max_temp","max_dew","max_humid"]
    
    ######processing train data
    
    for feature in (consider_features):
        for i in range(past_weather_interval,0, -1):
            n_col = feature+"-"+str(i)      #name of col, ***-10 to ***-1
            x_train[n_col] = -1             #init with value -1
            for idx in x_train.index:
                x_train.loc[idx,n_col] = train_df.iloc[idx + 30 - i][feature]  #assign the value
    
    for i in range(past_cases_interval,0, -1):
        n_col = "dailly_cases-"+str(i)
        x_train[n_col] = -1                 #init with -1
        for idx in x_train.index:
            x_train.loc[idx,n_col] = train_df.iloc[idx + 30 - i]['dailly_cases']
    train_features = x_train.columns.tolist()
            
    #drop the col 'day'
    x_train = x_train.drop(["day"], axis=1)
    y_train = y_train["dailly_cases"]
    #convert to np.array
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    
    #fit model
    svm_model.fit(x_train, y_train)
    
    #####processing test data
    test_fts = test_feature.index.tolist()
    for ft in test_fts:
        if ft not in train_features:
            test_feature = test_feature.drop([ft])
    test_feature = test_feature.drop(['day'])
    x_test = [np.array(test_feature)]       ##the shape should be [ [] ]
   
    
    return (math.floor(svm_model.predict(x_test)))



## Project-Part2
def predict_COVID_part2(train_df, train_labels_df, test_feature):
    pass ## Replace this line with your implementation

