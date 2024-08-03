# -*- coding: utf-8 -*-
"""SML ASSIGNMENT 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1P2vr0wZsBJ6MWH4c6Gv1KanhDtJQPqEq
"""

X=[2.3,2.5,3.6,2.8,3.1,2.9,3.2,2.7,2.8,3.0]

import matplotlib.pyplot as plt
plt.hist(X, bins=5, density=True)
plt.xlabel('X')
plt.ylabel('Density')
plt.title('Histogram of X')
plt.show()

import numpy as np
from scipy.stats import skew, kurtosis

x = np.array([4, 5, 8, 2, 4, 2, 5])
y = np.array([5, 6, 3, 8, 3, 7, 8])

import numpy as np
from scipy.stats import skew, kurtosis

x = np.array([4, 5, 8, 2, 4, 2, 5])
y = np.array([5, 6, 3, 8, 3, 7, 8])

def descriptive_stats(data):
    mean = np.mean(data)
    median = np.median(data)
    mode = np.argmax(np.bincount(data))
    variance = np.var(data)
    std_dev = np.std(data)
    data_range = np.max(data) - np.min(data)
    iqr = np.percentile(data, 75) - np.percentile(data, 25)
    skewness_val = skew(data)
    kurtosis_val = kurtosis(data)

    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)
    print("Variance:", variance)
    print("Standard Deviation:", std_dev)
    print("Range:", data_range)
    print("Interquartile Range (IQR):", iqr)
    print("Skewness:", skewness_val)
    print("Kurtosis:", kurtosis_val)


print("Descriptive Statistics for x:")
descriptive_stats(x)

print("\nDescriptive Statistics for y:")
descriptive_stats(y)

import pandas as pd

import numpy as np

from scipy.stats import skew,kurtosis

file_path = '/content/sample_data/california_housing_test.csv'

df = pd.read_csv(file_path)

def descriptive_stats(data):
    mean = np.mean(data)
    median = np.median(data)

    variance = np.var(data)
    std_dev = np.std(data)
    data_range = np.max(data) - np.min(data)
    iqr = np.percentile(data, 75) - np.percentile(data, 25)
    skewness_val = skew(data)
    kurtosis_val = kurtosis(data)

    print("Mean:", mean)
    print("Median:", median)
    print("Variance:", variance)
    print("Standard Deviation:", std_dev)
    print("Range:", data_range)
    print("Interquartile Range (IQR):", iqr)
    print("Skewness:", skewness_val)
    print("Kurtosis:", kurtosis_val)


for column in df.columns:
    print("\nDescriptive Statistics for", column, ":")
    descriptive_stats(df[column])