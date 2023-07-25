# import the required packages
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def function1():
    # source data
    temperatures = np.array([20, 23, 24, 25, 23, 26, 27, 29, 31, 32, 32, 34, 35, 36])

    # values to be shown on x-axis
    x_values = np.arange(temperatures.size)
    print(x_values)

    # draw a scatter plot
    plt.scatter(x_values, temperatures, color="red", label="Temperature")

    # add labels or title
    plt.xlabel("days")
    plt.ylabel("temperature")
    plt.title("Temperature Values")

    # add a legend
    plt.legend()

    plt.show()


# function1()


def function2():
    # source data
    temperatures = np.array([20, 23, 24, 25, 23, 26, 27, 29, 31, 32, 32, 34, 35, 36])
    x_values = np.arange(temperatures.size)

    # create a plot / line chart
    plt.plot(x_values, temperatures, label="Temperature")
    plt.scatter(x_values, temperatures, label="Temperature")

    # add labels/title
    plt.xlabel("Days")
    plt.ylabel("Temperatures")
    plt.title("Temperature Values")

    # add a legend()
    plt.legend()

    # show the chart
    plt.show()


# function2()


def function2():
    # read the data from Salary_Data
    df = pd.read_csv('Salary_Data.csv')

    # create a plot and scatter with
    # - x-axis: df['YearsExperience']
    # - y-axis: df['Salary']
    plt.plot(df['YearsExperience'], df['Salary'], label="Salary")
    plt.scatter(df['YearsExperience'], df['Salary'], label="Salary")

    # add legend()
    plt.legend()

    # add title
    plt.xlabel("Years of experience")
    plt.ylabel("Salary")
    plt.title("Salary vs Experience")

    # show the graph
    plt.show()


# function2()


def function3():
    # read the data from Salary_Data
    df = pd.read_csv('50_Startups.csv')

    x_values = np.arange(df['Profit'].size)

    # create a plot and scatter with
    plt.plot(x_values, df['RnD'], label="RnD")
    plt.scatter(x_values, df['RnD'])

    # create a plot and scatter with
    plt.plot(x_values, df['Marketing'], label="Marketing")
    plt.scatter(x_values, df['Marketing'])

    # create a plot and scatter with
    plt.plot(x_values, df['Administration'], label="Administration")
    plt.scatter(x_values, df['Administration'])

    # create a plot and scatter with
    plt.plot(x_values, df['Profit'], label="Profit")
    plt.scatter(x_values, df['Profit'])

    # add legend()
    plt.legend()

    # add title
    plt.xlabel("Companies")
    plt.ylabel("")
    plt.title("50 Startups")

    # show the graph
    plt.tight_layout()

    # save the graph to the disk
    plt.savefig('50_startups.png')

    plt.show()


# function3()


def function4():
    # read the data from Salary_Data
    df = pd.read_csv('50_Startups.csv')

    # create a plot and scatter with
    plt.plot(df['RnD'], df['Profit'], label="Profit")
    plt.scatter(df['RnD'], df['Profit'])

    # add legend()
    plt.legend()

    # add title
    plt.xlabel("RnD")
    plt.ylabel("Profit")
    plt.title("Profit vs RnD")

    # show the graph
    plt.tight_layout()

    plt.show()


# function4()


def function5():
    # read the data from Salary_Data
    df = pd.read_csv('50_Startups.csv')

    # create a plot and scatter with
    plt.plot(df['Marketing'], df['Profit'], label="Profit")
    plt.scatter(df['Marketing'], df['Profit'])

    # add legend()
    plt.legend()

    # add title
    plt.xlabel("Marketing")
    plt.ylabel("Profit")
    plt.title("Profit vs Marketing")

    # show the graph
    plt.tight_layout()

    plt.show()


# function5()

# plot: line chart
# scatter
# piechart
# barplot
# histogram
# boxplot
