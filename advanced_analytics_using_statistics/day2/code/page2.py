import numpy as np
import pandas as pd


def function1():
    # two dimensional collection
    cars = [
        {"model": "i20", "company": "hyudai", "price": 15, "fuel": "petrol"},
        {"model": "seltos", "company": "kia", "price": 19},
        {"model": "meridian", "company": "jeep", "price": 43}
    ]

    # data frame
    df = pd.DataFrame(cars)
    print(df)


# function1()


def function2():
    s1 = pd.Series({"model": "i20", "company": "hyudai", "price": 15, "fuel": "petrol"})
    s2 = pd.Series({"model": "seltos", "company": "kia", "price": 19})
    s3 = pd.Series({"model": "meridian", "company": "jeep", "price": 43})

    print(s1)
    print(s2)
    print(s3)

    cars = [
        {"model": "i20", "company": "hyudai", "price": 15, "fuel": "petrol"},
        {"model": "seltos", "company": "kia", "price": 19},
        {"model": "meridian", "company": "jeep", "price": 43}
    ]

    df = pd.DataFrame(cars)
    print(df)
    # for model
    # column1 = pd.Series(["i20", "seltos", "meridian"])
    #                      0       1         2

    # company
    # column2 = pd.Series(["hyndai", "kia", "jeep"])
    #                       0         1      2


# function2()


def function3():
    # two dimensional collection
    numbers = [
        [10, 20, 30, 40, 50],
        [60, 70, 80, 90, 100]
    ]

    df = pd.DataFrame(numbers, index=["r1", "r2"], columns=["col1", "col2", "col3", "col4", "col5"])
    print(df)

    numbers2 = [
        [10, 20],
        [30, 40],
        [50, 60],
        [70, 80],
        [90, 100]
    ]
    df2 = pd.DataFrame(numbers2)
    print(df2)


# function3()


def function4():
    # read data from a csv file
    df = pd.read_csv("Data.csv")
    # print(df)

    # get first 5 rows
    # head(df)
    # print(df.head())

    # get first 3 rows
    # head(df, 3)
    # print(df.head(3))

    # get last 5 rows
    # tail(df)
    # print(df.tail())

    # get last 3 rows
    # tail(df, 3)
    # print(df.tail(3))

    # get the column names
    # colnames(df)
    # print(df.columns)

    # get the general information
    # str(df)
    # df.info()

    # get the statistical information
    # summary(df)
    # print(df.describe())


# function4()


def function5():
    # read a file named titanic.csv
    df = pd.read_csv('titanic.csv')

    # get first 10 rows
    # print(df.head(10))

    # get last 10 rows
    # print(df.tail(10))

    # get the list of columns
    # print(df.columns)

    # get general information
    # df.info()

    # get statistical information
    # print(df.describe())

    # find if there are any NA values
    # print(df.isna())

    # find the number of na values per columns
    print(df.isna().sum())


# function5()




