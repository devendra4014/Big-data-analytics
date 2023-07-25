import numpy as np
import pandas as pd


def calculate_covariance(x, y):
    def calculate_mean(array):
        return sum(array) / len(array)

    # calculate the mean for x and y
    x_mean = calculate_mean(x)
    y_mean = calculate_mean(y)

    # x - xMean
    x_minus_mean = list(map(lambda v: v - x_mean, x))

    # y - yMean
    y_minus_mean = list(map(lambda v: v - y_mean, y))

    values = []
    for index in range(len(x_minus_mean)):
        values.append(x_minus_mean[index] * y_minus_mean[index])

    covariance_p = sum(values) / len(x)
    covariance_s = sum(values) / (len(x) - 1)
    print(f"covariance.p = {covariance_p}")
    print(f"covariance.s = {covariance_s}")


# calculate_covariance(
#     [10, 15, 18, 20, 25],
#     [18, 20, 30, 35, 40]
# )


def function1():
    a1 = np.array([10, 15, 18, 20, 25])
    a2 = np.array([18, 20, 30, 35, 40])

    # [cov(x, x)    cov(x, y)]
    # [cov(y, x)    cov(y, y)]
    covariance_matrix = np.cov(a1, a2)
    print(covariance_matrix)
    print(f"covariance = {covariance_matrix[0][1]}")

    correlation = np.corrcoef(a1, a2)
    print(correlation)


# function1()


def function2():
    df = pd.read_csv('Salary_Data.csv')

    covariance = np.cov(df['YearsExperience'], df['Salary'])
    print(covariance)

    correlation = np.corrcoef(df['YearsExperience'], df['Salary'])
    print(correlation)


function2()