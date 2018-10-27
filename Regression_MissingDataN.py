import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf
df=pd.read_csv("C:\\Users\\peyma\\PycharmProjects\\HW2\\celeb.csv",encoding="cp1252")
df.head()
df = df.replace(r'^\s+$', np.nan, regex=True)
df=df.dropna(axis=0, how='any')
