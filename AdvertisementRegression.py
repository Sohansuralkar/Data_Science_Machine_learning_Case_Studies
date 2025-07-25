import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


def MarvellousAdvertise(Datapath):
    df = pd.read_csv(Datapath)

    print("Dataset sample is : ")
    print(df.head())
    print("CLean the dataset")
    df.drop(columns = ["Unnamed: 0"] ,inplace = True)

    print("Updated dataset is :")
    print(df.head())

    print("Missing Values in each Column",df.isnull().sum())       # missing value display 

    print("Statitical summary ")
    print(df.describe())

    print("Corelation matrix ")    # corelation matrix matrix how it will work ..related with dependent variable and independent varible so interview questio 
    print(df.corr())
def main():
    MarvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()