import pandas as pd


def readCSV():
    df = pd.read_csv("TestData.csv")
    print(df)
    print("I am reading the excel file")