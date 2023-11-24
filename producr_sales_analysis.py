# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:26:55 2023

@author: Asus
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# visualization

import seaborn as sns

# Importing the dataset

dataset = pd.read_csv(r"C:\Users\Asus\Downloads\electronics.csv")

# list of first five rows

dataset.head()


dataset.tail()

# shape

dataset.shape

# It is also a good practice to know the columns and their corresponding data types
# along with finding whether they contain null values or not.

dataset.info()


# We can see that the dataset contains 5 columns and 10000 rows.    

# The columns are as follows:

# 1. User ID

# 2. Product ID

# 3. Rating

# 4. Timestamp

# 5. Category

# The data types of the columns are as follows:

# 1. User ID - int64

# 2. Product ID - object

# 3. Rating - int64

# 4. Timestamp - int64

# 5. Category - object

# We can see that the columns User ID and Rating are of int64 data type, while the columns Product ID and Category are of object data type.

# We can also see that there are no null values in the dataset.

# We can also see that the column Timestamp is of int64 data type, but it is actually a timestamp.

# We can convert it to a timestamp using the following code:

from datetime import datetime

pd.to_datetime(dataset['timestamp'])

# We can also see that the column Product ID is of object data type, but it is actually a string.

# We can convert it to a string using the following code:

dataset['brand'] = dataset['brand'].astype(str)
# We can also see that the column Category is of object data type, but it is actually a string.

# We can convert it to a string using the following code:

dataset['category'] = dataset['category'].astype(str)
# We can also see that the column Timestamp is of int64 data type, but it is actually a timestamp.

# We can convert it to a timestamp using the following code:

dataset['timestamp'] = pd.to_datetime(dataset['timestamp'])
# We can also see that the column Rating is of int64 data type, but it is actually a float.

# We can convert it to a float using the following code:

dataset['rating'] = dataset['rating'].astype(float)
# We can also see that the column User ID is of int64 data type, but it is actually a string.

# We can convert it to a string using the following code:

dataset['user_id'] = dataset['user_id'].astype(str)
# We can also see that the column Product ID is of object data type, but it is actually a string.

# We can convert it to a string using the following code:

dataset['item_id'] = dataset['item_id'].astype(str)
# to get a better understanding of the dataset,

# we can also see the statistical summary of the dataset.

dataset.describe()

# 1. The mean rating is 4.

# 2. The minimum rating is 1.

# 3. The maximum rating is 5.

# 4. The standard deviation of the ratings is 1.4.

# 5. The 25th percentile of the ratings is 4.

# 6. The 50th percentile of the ratings is 5.

# 7. The 75th percentile of the ratings is 5.
# We can also see the number of unique users and items in the dataset.

dataset.nunique()

# check for duplicates

dataset.duplicated().sum()

# check for missing values

dataset.isnull().sum()

# the distribution of ratings

dataset['rating'].value_counts()

# most of the ratings are 5
# what was the best year of sales

dataset['year'] = pd.DatetimeIndex(dataset['timestamp']).year

dataset['year'].value_counts()

# 2015 was the best year of sales
# what was the best month of sales

dataset['month'] = pd.DatetimeIndex(dataset['timestamp']).month

dataset['month'].value_counts()

# January was the best month of sales
# drop all null values

dataset.dropna(inplace=True)

# check for missing values


# FINDING ANSWERS WITH THE DATA WE HAVE WITH VISUALIZATIONS
# the distribution of ratings 

sns.countplot(x='rating', data=dataset)


# the distribution of ratings

# The distribution of ratings is as follows:

# most of the ratings are 5

dataset['rating'].value_counts()
      
# the distribution of sales by year

sns.countplot(x='year', data=dataset)

# the distribution of sales by year

# The distribution of sales by year is as follows:

# 2015 was the best year of sales
<AxesSubplot:xlabel='year', ylabel='count'>

# brands with the most sales

sns.countplot(x='brand', data=dataset, order=dataset['brand'].value_counts().iloc[1:10].index)


# What brand name sold the least?

sns.countplot(x='brand', data=dataset, order=dataset['brand'].value_counts().iloc[-10:].index)

# We can see that the brand name of EINCAR sold the least followed closely with DURAGADGET.
# Logitech & Bose had the most sales followed by Sony.
# brands with the most sales in 2016

sns.countplot(x='brand', data=dataset[dataset['year'] == 2016], order=dataset['brand'].value_counts().iloc[1:10].index)


# in 2016 Bose overtook Logitech to have the most sales.

# TaoTronics had the third most sales that year
# brands with the most sales in 2017

sns.countplot(x='brand', data=dataset[dataset['year'] == 2017], order=dataset['brand'].value_counts().iloc[1:10].index)


# the top 3 products sold in 2017 were Bose, Logitech and Mpow.
# brands with the most sales in 2018

sns.countplot(x='brand', data=dataset[dataset['year'] == 2018], order=dataset['brand'].value_counts().iloc[1:10].index)


# For 2018, Bose was the most sold for a third year in a row followed by Logitech while Mpow was the third most sold.
# month with most sales

sns.countplot(x='month', data=dataset)


# January[#1] was the month with the most sales
# What products by category were sold the most in January

sns.countplot(x='category', data=dataset[dataset['month'] == 1], order=dataset['category'].value_counts().iloc[1:10].index)


# The top 3 products sold in January were Computers & Accesories, Camera & Photo and Accesories & Supplies.
# Category with the least sales

sns.countplot(x='category', data=dataset, order=dataset['category'].value_counts().iloc[-10:].index)


# The category with the least sales was Security & Surveillance while the most sales were Headphones.
# distribution of sales presented in a pie chart

dataset['category'].value_counts(normalize=True)
dataset.groupby('category')['rating'].count().sort_values(ascending=False).head(10).plot(kind='pie')

# white background

sns.set_style('white')

# conclusion of our analysis

# We can see that the year 2015 had the best sales.

# The month of January had the best sales.

# We can see that the brands Bose and Logitech sold the most

# We can see that the category of Headphones sold the most.

# We can see that the brand name of EINCAR sold the least followed closely with DURAGADGET.

# We can see that the category of Security and Surveillance sold the least.