"""
Calculations library
"""
# imports
import pandas as pd
#import matplotlib.pyplot as plt

def mean_variable(path, variable):
    df = pd.read_csv(path)
    return df[variable].mean()

def median_variable(path, variable):
    df = pd.read_csv(path)
    return df[variable].median()

def count_variable(path, variable):
    df = pd.read_csv(path)
    return df[variable].sum() / df[variable].mean() 
