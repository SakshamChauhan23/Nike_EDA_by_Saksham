#Importing required Libraries
from turtle import color
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#Importing dataset
df = pd.read_csv(r'C:\Users\SAKSHAM\Desktop\Coding\Nike\nike_data_2022_09.csv')

#Understanding the dataset
df.head(5)
df.columns
df.shape

#Checking up the null values
df.isna().sum()

#Data Cleaning
"""Let's get started with dropping unnecessary columns"""
df.drop(['url','model','description','raw_description','images','uniq_id','scraped_at'],axis=1,inplace=True)
df.head(5)

"""Let's deal with the null values"""
df['avg_rating']= df['avg_rating'].fillna(df['avg_rating'].median(),axis=0)
df.drop('review_count',axis=1,inplace=True)
df['color']=df['color'].fillna(df['color'].mode()[0])
df['availability']=df['availability'].fillna(df['availability'].mode()[0])
df['available_sizes']=df['available_sizes'].fillna(df['available_sizes'].mode()[0])

"""Statistic Summary"""
df.describe(include=object)
df.isna().sum()

#Exploration Begins

"""Price Distribution"""
plt.figure(figsize=(12,8))
avg_price = df['price'].mean()
plt.axvline(avg_price, 0,1, color='red')
sns.distplot(df['price'], color='blue')
#plt.show()

"""Average rating Distribution"""
plt.figure(figsize=(12,8))
avg_ratings = df['avg_rating'].mean()
plt.axvline(avg_ratings, 0,1, color='purple')
sns.distplot(df['avg_rating'], color='blue')
#plt.show()

"""Color Distributions"""
color = df['color'].value_counts()[:5]
plt.figure(figsize=(12,6))
ax= sns.barplot(x=list(color.keys()),y=list(color.values),palette='Blues')
for container in ax.containers:
    ax.bar_label(container)