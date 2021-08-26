# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 10:12:22 2021

@author: yihsuan.liu
"""
import os
os.environ["KMP_DUPLICATE_LIB_OK"]  =  "TRUE"
import glob2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch 
from torch.utils.data import Dataset,DataLoader
from sklearn.decomposition import PCA
from statsmodels.tsa.arima_model import ARIMA
from sklearn import datasets
from sklearn import preprocessing
import numpy as np, pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
import matplotlib as mpl
from pandas.plotting import lag_plot

path='C:\\Users\\yihsuan.liu\\Documents\\IAI\\raw data\\'

'''匯入預測資料'''
Wear_A=pd.read_csv(path+'Train_A_wear.csv').drop(columns='cut')
Wear_B=pd.read_csv(path+'Train_B_wear.csv').drop(columns='cut')

'''標準化samples'''
def Standardization(PATH,SET):
    DF=pd.read_excel(PATH,sheet_name=SET)
    columns=DF.columns
    DF = pd.DataFrame(preprocessing.scale(DF))
    DF.columns=columns
    return DF
TrainSets=['Train_A','Train_B','Test']
Train_A=Standardization(path+'特徵擷取.xlsx',TrainSets[0])
Train_B=Standardization(path+'特徵擷取.xlsx',TrainSets[1])
Test=Standardization(path+'特徵擷取.xlsx',TrainSets[2])

'''主成分個數為7可解釋90%變異
add=0
for idx in range(len(var)):
    add+=var[idx]
    if add>=0.9:
        print(add,'index：',idx)
        break
pca.n_components_
var=pca.explained_variance_ratio_'''
#用scree plot 看解釋變異
pca= PCA(n_components=7)
x_labels=['PC1', 'PC2','PC3','PC4','PC5','PC6','PC7']
pca.fit_transform(Test)
var=pca.explained_variance_ratio_.tolist()
cum_var=np.cumsum(var).tolist()
plt.plot(x_labels, list(var), marker='o', markersize=6, color='skyblue', linewidth=2, label='Proportion of variance')
plt.plot(x_labels, list(cum_var), marker='o', color='orange', linewidth=2, label="Cumulative variance")
plt.legend()
plt.title('Test Scree plot')
plt.xlabel('Principal components')
plt.ylabel('Proportion of variance')
plt.show()
plt.close()


TrainA = pd.DataFrame(data = pca.fit_transform(Train_A), columns = ['PC1', 'PC2','PC3','PC4','PC5','PC6','PC7'])
TrainB = pd.DataFrame(data = pca.fit_transform(Train_B), columns = ['PC1', 'PC2','PC3','PC4','PC5','PC6','PC7'])
Test = pd.DataFrame(data = pca.fit_transform(Test), columns = ['PC1', 'PC2','PC3','PC4','PC5','PC6','PC7'])
y_trainA=Wear_A.min(axis = 1).to_frame().rename(columns={0 :'y'}, inplace = False)
y_trainB=Wear_B.min(axis = 1).to_frame().rename(columns={0 :'y'}, inplace = False)
TrainA = pd.concat([TrainA, y_trainA], axis = 1)
TrainB = pd.concat([TrainB, y_trainB], axis = 1)
#TrainA['Set']='A'
#TrainB['Set']='B'
#train = TrainA.append(TrainB,ignore_index=True)

mycolors = np.random.choice(list(mpl.colors.XKCD_COLORS.keys()), len(x_labels), replace=False)
lines=[]
plt.figure()
for i,x in enumerate(x_labels):        
        #lines+=plt.plot(Test[x])
        plot_pacf(Test[x])
        plt.title('Test '+x+' PACF')
        plt.show()

plt.legend(lines, x_labels,bbox_to_anchor=(1.0, 1.0))
plt.title('Test -PCA')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Import Statsmodels
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
from statsmodels.tools.eval_measures import rmse, aic
from statsmodels.tsa.stattools import grangercausalitytests
maxlag=12
test = 'ssr_chi2test'
def grangers_causation_matrix(data, variables, test='ssr_chi2test', verbose=False):    
    """Check Granger Causality of all possible combinations of the Time series.
    The rows are the response variable, columns are predictors. The values in the table 
    are the P-Values. P-Values lesser than the significance level (0.05), implies 
    the Null Hypothesis that the coefficients of the corresponding past values is 
    zero, that is, the X does not cause Y can be rejected.

    data      : pandas dataframe containing the time series variables
    variables : list containing names of the time series variables.
    """
    df = pd.DataFrame(np.zeros((len(variables), len(variables))), columns=variables, index=variables)
    for c in df.columns:
        for r in df.index:
            test_result = grangercausalitytests(data[[r, c]], maxlag=maxlag, verbose=False)
            p_values = [round(test_result[i+1][0][test][1],4) for i in range(maxlag)]
            if verbose: print(f'Y = {r}, X = {c}, P Values = {p_values}')
            min_p_value = np.min(p_values)
            df.loc[r, c] = min_p_value
    df.columns = [var + '_x' for var in variables]
    df.index = [var + '_y' for var in variables]
    return df

grangers_causation_matrix(TrainA, variables = TrainA.columns)
grangers_causation_matrix(TrainB, variables = TrainB.columns)
grangers_causation_matrix(Test, variables = Test.columns)
from statsmodels.tsa.vector_ar.vecm import coint_johansen

def cointegration_test(df, alpha=0.05): 
    """Perform Johanson's Cointegration Test and Report Summary"""
    out = coint_johansen(df,-1,5)
    d = {'0.90':0, '0.95':1, '0.99':2}
    traces = out.lr1
    cvts = out.cvt[:, d[str(1-alpha)]]
    def adjust(val, length= 6): return str(val).ljust(length)

    # Summary
    print('Name   ::  Test Stat > C(95%)    =>   Signif  \n', '--'*20)
    for col, trace, cvt in zip(df.columns, traces, cvts):
        print(adjust(col), ':: ', adjust(round(trace,2), 9), ">", adjust(cvt, 8), ' =>  ' , trace > cvt)

cointegration_test(Test)

def adfuller_test(series, signif=0.05, name='', verbose=False):
    """Perform ADFuller to test for Stationarity of given series and print report"""
    r = adfuller(series, autolag='AIC')
    output = {'test_statistic':round(r[0], 4), 'pvalue':round(r[1], 4), 'n_lags':round(r[2], 4), 'n_obs':r[3]}
    p_value = output['pvalue'] 
    def adjust(val, length= 6): return str(val).ljust(length)

    # Print Summary
    print(f'    Augmented Dickey-Fuller Test on "{name}"', "\n   ", '-'*47)
    print(f' Null Hypothesis: Data has unit root. Non-Stationary.')
    print(f' Significance Level    = {signif}')
    print(f' Test Statistic        = {output["test_statistic"]}')
    print(f' No. Lags Chosen       = {output["n_lags"]}')

    for key,val in r[4].items():
        print(f' Critical value {adjust(key)} = {round(val, 3)}')

    if p_value <= signif:
        print(f" => P-Value = {p_value}. Rejecting Null Hypothesis.")
        print(f" => Series is Stationary.")
    else:
        print(f" => P-Value = {p_value}. Weak evidence to reject the Null Hypothesis.")
        print(f" => Series is Non-Stationary.")    

for name, column in TrainB.iteritems():
    adfuller_test(column, name=column.name)
    print('\n')
df_differenced = TrainB.diff().dropna()
# ADF Test on each column of 1st Differences Dataframe
for name, column in df_differenced.iteritems():
    adfuller_test(column, name=column.name)
    print('\n')

# Second Differencing
df_differenced = df_differenced.diff().dropna()
# ADF Test on each column of 2nd Differences Dataframe
for name, column in df_differenced.iteritems():
    adfuller_test(column, name=column.name)
    print('\n')

model = VAR(df_differenced)
for i in [1,2,3,4,5,6,7,8,9]:
    result = model.fit(i)
    print('Lag Order =', i)
    print('AIC : ', result.aic)
    print('BIC : ', result.bic)
    print('FPE : ', result.fpe)
    print('HQIC: ', result.hqic, '\n')
    
model = VAR(endog=TrainA)
model_fit = model.fit()
# make prediction on validation
prediction = model_fit.forecast(model_fit.y, steps=len(Test))
#converting predictions to dataframe
pred = pd.DataFrame(index=range(0,len(prediction)),columns=[cols])
for j in range(0,7):
    for i in range(0, len(prediction)):
       pred.iloc[i][j] = prediction[i][j]
cols = TrainA.columns
#check rmse
from sklearn.metrics import mean_squared_error
for i in cols:
    print('rmse value for', i, 'is : ', (mean_squared_error(pred[i], Test[i]))**0.5)



#用回歸找出特徵的y再做arima
import statsmodels.formula.api as smf
modelA = smf.ols('y~PC1+PC2+PC3+PC4+PC5+PC6+PC7',data=TrainA).fit()
predictionsA = model.predict(Test) 
print_modelA = modelA.summary()
print(print_modelA)
modelB = smf.ols('y~PC1+PC2+PC3+PC4+PC5+PC6+PC7',data=TrainB).fit()
predictionsB = model.predict(Test) 
print_modelB = modelB.summary()
print(print_modelB)
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from pmdarima.arima import ndiffs
plot_pacf(TrainA["PC1"])
plt.show()

# 算出推薦的差分次數
d =  ndiffs(TrainA["PC2"],  test="adf")
print(d) # 1

#  觀察PACF圖，參數是差分之後的資料
plot_pacf(TrainA["PC1"].diff(1))
plt.show()

#  觀察ACF圖，參數是差分之後的資料
plot_acf(TrainA["PC1"].diff(1))
plt.show()
