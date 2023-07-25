import numpy as np
import pandas as pd


def function1():
    df = pd.read_csv('titanic.csv')

    # get the columns
    print(df.columns)

    # delete a column from a df
    # when you use del,
    # - the same df gets modified
    # - you need to delete multiple columns one by one
    del df['body']
    del df['boat']
    print(df.columns)

    # remove a column
    # returns a new df by deleting the column
    # df_new = df.drop('embarked', axis=1)
    df_new = df.drop(['embarked', 'cabin', 'fare'], axis=1)
    print(df_new.columns)

    # remove multiple columns by updating same df
    df.drop(['age', 'sibsp', 'parch', 'ticket'], axis=1, inplace=True)
    print(df.columns)


# function1()


def function2():
    df = pd.read_csv('nba.csv')

    # print all columns
    print(df.columns)

    # remove college, weight and height one by one using del
    del df['College']
    del df['Weight']
    del df['Height']
    print(df.columns)

    # remove team, salary using drop by creating new data frame
    df_new = df.drop(['Team', 'Salary'], axis=1)
    print(df.columns)
    print(df_new.columns)

    # remove number and name from the same df
    df.drop(['Number', 'Name'], axis=1, inplace=True)
    print(df.columns)


# function2()


def function3():
    df = pd.read_csv('Data.csv')
    print(df.columns)

    # add a new column named SalaryAfterBonus
    df['SalaryAfterBonus'] = 10000 + df.Salary
    print(df)

    # delete a column named Purchase
    del df['Purchased']
    print(df)

    # save the changes on the disk
    df.to_csv('new_data.csv')


# function3()


def function4():
    # read nba file
    df = pd.read_csv('nba.csv')

    # remove Team, Name and College
    df.drop(['Team', 'Name', 'College'], axis=1, inplace=True)

    # add column named Bonus with value 15000
    df['Bonus'] = 15000

    # add column named NewSalary with formula existingSalary + bonus
    df['NewSalary'] = df['Bonus'] + df['Salary']

    # persist the changes on disk
    df.to_csv('new_nba.csv')


# function4()


# if the data is having missing records then
# - if a row is having many columns with NA values then its
#   better to delete the entire row
# - if a column is having many missing values, then its better
#   to delete the entire column
# - if the missing values are less than 10 to 20 % of the column
#   its better to replace them with mean / average of the column


def function5():
    df = pd.read_csv('titanic.csv')
    print(f"missing values = {df['body'].isna().sum()}")

    mean = df['body'].mean()
    print(f"mean of body column = {mean}")

    # replace the na / missing values with the mean value of the column
    # df['body'] = df['body'].fillna(mean)
    df['body'].fillna(mean, inplace=True)

    print(df)


# function5()


def function6():
    # read nba
    df = pd.read_csv('nba.csv')

    # replace the na values of Salary and Age
    df['Salary'].fillna(df.Salary.mean(), inplace=True)
    df['Age'].fillna(df.Age.mean(), inplace=True)

    print(f"no if NA values in Salary = {df.Salary.isna().sum()}")
    print(f"no if NA values in Age = {df.Age.isna().sum()}")

    # save the changes to the disk
    df.to_csv('new_nba.csv')


function6()

