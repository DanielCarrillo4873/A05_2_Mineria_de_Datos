from sklearn.model_selection import train_test_split
import pandas as pd
import random

def dataframe_zero_r():
    df = pd.read_csv("cancer_zero_r.csv")
    train, test = train_test_split(df, test_size=0.3)
    print(train)
    print(test)