import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf
df=pd.read_csv("C:\\Users\\peyma\\PycharmProjects\\HW2\\TEST_missing.csv",encoding="cp1252")
df.head()
newdf=df.dropna(how='any')
newdf.head()
X= newdf[['Hemoglobin','Albumin','WhiteBC','BP_sys','BP_dia']]
Y=newdf['FVC']
mod = smf.ols('Y ~ X', data=newdf)
res = mod.fit()
print(res.summary())