# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:28:00 2023

@author: Lenovo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


df=pd.read_csv("/content/Unemployment in India.csv")

df.head()
df.tail()
df.shape
df.size
df.isna().sum()
df.dropna(inplace=True)
df.shape
df.size
df.info()
df.describe(include='all')
df.columns
df.columns=df.columns.str.strip()
df.columns=df.columns.str.replace(' ','_')
df.columns
df['Region'].value_counts()
px.bar(df,x=df['Region'].value_counts().keys(),y=df['Region'].value_counts(),color=df['Region'].value_counts().keys(),title='Region Counts')
px.pie(df,names=df['Region'].value_counts().keys(),values=df['Region'].value_counts(),color=df['Region'].value_counts().keys(),title='Region %age')
df['Area'].value_counts()
px.bar(df,x=df['Area'].value_counts().keys(),y=df['Area'].value_counts(),color=df['Area'].value_counts().keys(),title='Area Counts')
px.pie(df,names=df['Area'].value_counts().keys(),values=df['Area'].value_counts(),color=df['Area'].value_counts().keys(),title='Area %age')
import datetime as dt
df.head()
