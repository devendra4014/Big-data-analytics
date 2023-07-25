# indexing
import numpy as np


def function1():
    a1 = np.arange(1, 11) * 5
    print(a1)

    # positive
    print(f"a1[0] = {a1[0]}")

    # negative
    print(f"a1[-1] = {a1[-1]}")


# function1()


def function2():
    # array
    a1 = np.array([10, 20, 30, 40, 50])

    # get multiple values using index positions
    # [10, 40, 50]
    print(a1[[0, 3, 4]])

    # get multiple values using boolean array
    # [10, 40, 50]
    print(a1[[True, False, False, True, True]])

    # get all the values greater than 25
    # filtering
    print(f"a1 > 25 = {a1 > 25}")
    print(a1[a1 > 25])


# function2()


# slicing

def function3():
    a1 = np.array([10, 20, 30, 40, 50])

    # [10, 20, 30]
    print(f"a1[0:3] = {a1[0:3]}")
    print(f"a1[:3]  = {a1[:3]}")

    # [30, 40, 50]
    print(f"a1[2:5] = {a1[2:5]}")
    print(f"a1[2:]  = {a1[2:]}")

    # [10, 20, 30, 40, 50]
    print(f"a1[0:5] = {a1[0:5]}")
    print(f"a1[:]   = {a1[:]}")


# function3()


def function4():
    a1 = np.array([23, 25, 49, 60, 70, 90, 98, 67, 89])

    # [23, 25, 49]
    # use positive, negative and boolean indexing
    print(a1[[0, 1, 2]])
    print(a1[[-9, -8, -7]])
    print(a1[[True, True, True, False, False, False, False, False, False]])

    # find out the values less than 40
    print(a1[a1 < 40])

    # find out the values greater than 35
    print(a1[a1 > 35])

    # use positive, negative and boolean indexing
    # [98, 67, 89]
    # [25, 49, 60, 70]


function4()
