import numpy as np
import pandas as pd


def function1():
    df = pd.read_csv('Data.csv')

    # get the columns names
    print(df.columns)

    # get the Salary from df
    # returns a series object
    # print(df['Salary'])
    print(df.Salary)

    # get the Country and Salary
    # returns data frame
    # print(df[['Country', 'Salary']])


# function1()


def function2():
    df = pd.read_csv('Data.csv')

    # get na values from Salary column
    print(df.Salary.isna())

    # get the count of na values of Salary column
    print(df.Salary.isna().sum())

    # read titanic
    # get the na values from body column
    # get the count of na values from body column


# function2()


def function3():
    # aggregate functions
    # - work on the whole data

    df = pd.read_csv('Data.csv')

    # find the minimum value in Salary column
    print(f"minimum: {df.Salary.min()}")

    # find the maximum value in Salary column
    print(f"maximum: {df.Salary.max()}")

    # find the mean value of salary column
    print(f"average: {df.Salary.mean()}")

    # find the sum of salary column
    print(f"sum: {df.Salary.sum()}")

    # find the number of rows in Salary column
    print(f"count: {df.Salary.count()}")

    print()

    # get the minimum value for every column
    print(df.min())

    print()

    # get max for every column
    print(df.max())

    print()

    # get the mean of every numeric column
    print(df.mean(numeric_only=True))

    print()

    print(df.sum())

    print()

    print(df.count())

    print()

    print(df.describe())

    # read 50_Startups.csv
    # find the count of missing values from every column

    # find the row count of every column
    # find the min, max and sum of every column

    # find the row count of Administration column
    # find the min, max and sum of Profit column


# function3()


def function4():
    df = pd.read_csv('50_Startups.csv')

    # get the columns
    # print(df.columns)

    # get all the rows from RnD column
    # print(df.RnD)

    # get the first row from RnD column
    print(df.RnD[0])
    print(df['RnD'][0])

    print()

    # get first 4 rows of RnD
    print(df.RnD[[0, 1, 2, 3]])
    print(df['RnD'][[0, 1, 2, 3]])

    print()

    # get all the rows with RnD and Administration
    print(df[['RnD', 'Administration']])


# function4()


def function5():
    df = pd.read_csv('50_Startups.csv')
    # print(df)

    # iloc
    # - used to get values by providing both row and column positions
    # - the first value is the row position(s)
    # - the second value is the columns position(s)

    # get the row 0 and Adminstration columns
    # print(df.iloc[0, 1])

    # first 10 rows with Administration column
    # print(df.iloc[0:10, 1])

    # get the first 10 rows with RnD, Administration and Marketing
    # print(df.iloc[0:10, 0:3])
    # print(df.iloc[:10, :3])

    # get last 10 rows with all columns
    print(df.iloc[-10:, :])


function5()















