import numpy as np
import pandas as pd


def function1():
    # list
    l1 = [10, 20, 30, 40, 50]
    print(l1)
    print(type(l1))

    print()

    # tuple
    t1 = (10, 20, 30, 40, 50)
    print(t1)
    print(type(t1))

    print()

    # array
    a1 = np.array([10, 20, 30, 40, 50])
    print(a1)
    print(type(a1))

    print()

    # series
    s1 = pd.Series([10, 20, 30, 40, 50])
    print(s1)
    print(type(s1))


# function1()


def function2():
    # one dimensional array
    s1 = pd.Series([10, 20, 30, 40, 50])
    print(s1)
    print(f"data type of every item in s1 = {s1.dtype}")
    print(f"size of s1 = {s1.size}")
    print(f"total memory needed = {s1.nbytes}")
    print(f"item size of s1 = {s1.nbytes // s1.size}")
    print(f"n dimension = {s1.ndim}")
    print(f"shape of s1 = {s1.shape}")
    print()
    print(f"index = {s1.index}")
    print(f"values = {s1.values}")


# function2()


def function3():
    # create series using list
    s1 = pd.Series([10, 20, 30, 40, 50])
    print(s1)
    print(f"value stored on 2nd position: {s1[2]}")

    print()

    # create series using tuple
    s2 = pd.Series((10, 20, 30, 40, 50))
    print(s2)

    print()

    # CAN NOT create series using set
    # s3 = pd.Series({10, 20, 30, 40, 50})
    # print(s3)

    # create series using dictionary
    s4 = pd.Series({"name": "person1", "address": "pune", "email": "p1@t.com"})
    print(s4)
    print(f"email of person = {s4['email']}")


# function3()


def function4():
    # lists
    models = ["i20", "seltos", "meridian", "X7"]
    companies = ["hyundai", "kia", "jeep", "bmw"]

    # create the series to store models
    s1 = pd.Series(models)
    print(s1)

    print()

    # create the series to store companies
    s2 = pd.Series(companies)
    print(s2)

    print()

    # create the series to store models using companies as index positions
    s3 = pd.Series(models, index=companies)
    print(s3)
    print(f"model of jeep = {s3['jeep']}")
    print(f"model of bmw  = {s3['bmw']}")

    print()

    s4 = pd.Series(companies, index=models)
    print(s4)
    print(f"company of seltos = {s4['seltos']}")


# function4()


def function5():
    # lists
    models = ["i20", "i10", "sonet", "seltos", "meridian", "compass", "X7", "x3"]
    companies = ["hyundai", "hyundai", "kia", "kia", "jeep", "jeep", "bmw", "bmw"]

    s1 = pd.Series(models, index=companies)
    print(s1)

    # returns a new series object with multiple values
    print(f"models of hyundai = {s1['hyundai']}")


# function5()


def function6():

    # create a series using a list of int values
    # create a series using a tuple of int values

    # create a series using dictionary
    # {"model": "iPhone", "company": "Apple", "price": 144000}


    s1 = pd.Series([23, 45, 29, 30, 10, 29, 19, 38])

    # positive indexing
    # get the values at index 0, 2, 4, and 6
    # get the value at 100th position

    # negative indexing
    # get the values at index -1, -4, -5, -7
    # get the value at -100th position

    # slicing
    # [29, 30, 10, 29]
    # [23, 45, 29, 30]
    # [29, 19, 38]

    # filtering
    # find the values greater than 20
    # find the values less than 23


