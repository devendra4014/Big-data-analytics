# import numpy package
import numpy as np
import sys


def function1():
    # list
    l1 = [10, 20, 30, 40, 50]
    print(f"l1 = {l1}, type = {type(l1)}")

    # array
    a1 = np.array([10, 20, 30, 40, 50])
    print(f"a1 = {a1}, type = {type(a1)}")


# function1()


def function2():
    # list
    l1 = [10, 20, 30, 40, 50, 60]
    print(f"memory size of every item = {sys.getsizeof(l1[0])} bytes")
    print(f"type of l1[0] = {type(l1[0])}")
    print(f"total memory needed = {sys.getsizeof(l1[0]) * len(l1)} bytes")

    print()

    # one dimensional array
    a1 = np.array([10, 20, 30, 40, 50, 60])
    print(f"a1 = {a1}")
    print(f"length of a1 = {a1.size}")
    print(f"memory size of every item = {a1.itemsize} bytes")
    print(f"total memory needed = {a1.itemsize * a1.size} bytes")
    print(f"shape of array = {a1.shape}")
    print(f"flags = {a1.flags}")


# function2()


def print_details(array):
    print(f"array = {array}")
    print(f"number of dimensions = {array.ndim}")
    print(f"type of array item = {array.dtype}")
    print(f"length of array = {array.size}")
    print(f"memory size of every item = {array.itemsize} bytes")
    print(f"total memory needed = {array.itemsize * array.size} bytes")
    print(f"total memory needed = {array.nbytes} bytes")
    print(f"shape of array = {array.shape}")
    print('-' * 80)


def function3():
    # itemsize = 8 bytes => int64
    a1 = np.array([10, 20, 30, 40, 50, 60])
    print_details(a1)

    # itemsize = 8 bytes => int64
    a2 = np.array([10, 20, 30, 40, 50, 60], dtype=np.int64)
    print_details(a2)

    # itemsize = 4 bytes => int32
    a3 = np.array([10, 20, 30, 40, 50, 60], np.int32)
    print_details(a3)

    # itemsize = 2 bytes => int16
    a4 = np.array([10, 20, 30, 40, 50, 60], np.int16)
    print_details(a4)

    # itemsize = 1 bytes => int8
    a5 = np.array([10, 20, 30, 40, 50, 60], np.int8)
    print_details(a5)


# function3()


def function4():
    # array of int values
    a1 = np.array([10, 20, 30, 40, 50])
    print_details(a1)

    # array of float values
    a2 = np.array([10.40, 20.30, 40.50, 50.60])
    print_details(a2)

    # array of string values
    a3 = np.array(["india", "usa", "uk"])
    print_details(a3)


# function4()


def function5():
    a1 = np.array([10, 20, 30, 40, 50, 60])
    print_details(a1)

    # every row must have same number of columns
    a2 = np.array([
        [10, 20],
        [30, 40],
        [50, 60]
    ])
    print_details(a2)

    # 3 dimensional collection
    a3 = np.array([
        [
            [10, 20, 80, 180],
            [30, 40, 90, 180],
            [120, 130, 140, 180]
        ],
        [
            [50, 60, 100, 180],
            [70, 80, 110, 180],
            [150, 160, 170, 180]
        ]
    ])
    print_details(a3)


function5()