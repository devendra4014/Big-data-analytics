import numpy as np


def function1():
    # array
    a1 = np.array([10, 20, 30, 40, 50, 60])
    print(a1)

    # arange
    a2 = np.arange(0, 10)
    print(a2)

    # arange
    a3 = np.arange(0, 10, 2)
    print(a3)

    # ones
    a4 = np.ones(5)
    print(a4)

    # zeros
    a5 = np.zeros(5)
    print(a5)


# function1()


def function2():
    # array of 5 1.0 float values
    a1 = np.ones(5)
    print(a1)

    # array of 5 integer values
    a2 = np.ones(5, dtype=np.int8)
    print(a2)

    # two dimensional array of size (2, 3)
    a3 = np.ones([2, 3])
    print(a3)

    # two dimensional array of size (2, 3)
    a4 = np.ones([2, 3], dtype=np.int8)
    print(a4)

    # three dimensional array
    a5 = np.ones([2, 3, 4], dtype=np.int8)
    print(a5)


# function2()


def function3():
    # returns an array with 5 random float values (0-1)
    a1 = np.random.random(5)
    print(a1)

    # array with 5 int values between 1 to 10
    # param1: lower bound
    # param2: upper bound
    # param3: size (one value or list of dimensions)
    a2 = np.random.randint(1, 10, 5)
    print(a2)

    a3 = np.random.randint(1, 100, [3, 5])
    print(a3)


# function3()


def function4():
    # one dimensional array
    a1 = np.array([10, 20, 30, 40, 50, 60])
    print(a1)

    # two dimensional array with shape (2, 3)
    a2 = a1.reshape([2, 3])
    print(a2)

    # two dimensional array with shape (3, 2)
    a3 = a1.reshape([3, 2])
    print(a3)

    # two dimensional array with shape (6, 1)
    a4 = a1.reshape([6, 1])
    print(a4)

    # two dimensional array with shape (1, 6)
    a5 = a1.reshape([1, 6])
    print(a5)


function4()


def function5():

    # create one dimensional array with 10 random int values
    a1 = np.random.randint(20, 30, 10)
    print(a1)

    # create two dimensional array with (4, 5) random int values
    a2 = np.random.randint(1, 20, [4, 5])
    print(a2)

    # create a two dimensional (2, 5) array from one dimensional array of size 10
    a3 = a1.reshape([2, 5])
    print(a3)

    # create a two dimensional (5, 2) array from one dimensional array of size 10
    a4 = a1.reshape([5, 2])
    print(a4)

    # create a two dimensional (5, 1) array from one dimensional array of size 5
    a5 = np.random.randint(1, 10, 5)
    a6 = a5.reshape([5, 1])
    print(a6)


# function5()