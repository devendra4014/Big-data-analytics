import numpy as np
import pandas as pd


def function1():
    # series with a list
    s1 = pd.Series([10, 20, 30, 40, 50])
    print(s1)

    # series with tuple
    s2 = pd.Series((10, 20, 30, 40, 50))
    print(s2)

    # series can not be created with set
    # s3 = pd.Series({10, 20, 30, 40, 50})
    # print(s3)

    # series with a dictionary (one dimensional)
    s4 = pd.Series({"model": "i20", "company": "hyudai", "price": 15.5})
    print(s4)


# function1()


def function2():
    # multi-dimensional collection
    cars = [
        {"model": "i20", "company": "hyudai", "price": 15},
        {"model": "seltos", "company": "kia", "price": 19},
        {"model": "meridian", "company": "jeep", "price": 43}
    ]

    # because the cars is a multi-dimensional collection
    # a series object can not be built with it
    s1 = pd.Series(cars)
    print(s1)


function2()

