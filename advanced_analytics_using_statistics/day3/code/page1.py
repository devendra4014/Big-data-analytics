def calculate_mean(values):
    addition = 0
    for value in values:
        addition += value
    mean = addition / len(values)
    print(f"mean = {mean}")


# calculate_mean([10, 20, 30, 40, 50])


def calculate_mode_v1(values):
    dictionary = {}
    for value in values:
        if dictionary.get(value) == None:
            dictionary[value] = 1
        else:
            dictionary[value] += 1
    print(dictionary)

    # get the frequencies from the dictionary
    frequencies = list(dictionary.values())
    print(frequencies)

    # get the keys (values from the input collection)
    keys = list(dictionary.keys())
    print(keys)

    # find the max frequency
    max_frequency = 0
    max_frequency_index = -1
    for index in range(len(frequencies)):
        if frequencies[index] > max_frequency:
            # found the max value
            max_frequency = frequencies[index]

            # set the index to the max value
            max_frequency_index = index

    print(f"max frequency: {max_frequency}, index : {max_frequency_index}")
    print(f"mode = {keys[max_frequency_index]}")


def calculate_mode_v2(values):
    dictionary = {}
    for value in values:
        if dictionary.get(value) == None:
            dictionary[value] = 1
        else:
            dictionary[value] += 1
    print(dictionary)

    # get the frequencies from the dictionary
    frequencies = list(dictionary.values())
    print(frequencies)

    # get the keys (values from the input collection)
    keys = list(dictionary.keys())
    print(keys)

    # find the max frequency
    max_frequency = 0
    for index in range(len(frequencies)):
        if frequencies[index] > max_frequency:
            max_frequency = frequencies[index]

    # used to collect the index positions of max frequency
    max_frequency_index_positions = []
    for index in range(len(frequencies)):
        if frequencies[index] == max_frequency:
            max_frequency_index_positions.append(index)

    # collect the mode values
    mode_values = []
    for index in max_frequency_index_positions:
        mode_values.append(keys[index])

    if len(mode_values) == len(values):
        print(f"no mode")
    else:
        print(f"mode = {mode_values}")


# single mode
calculate_mode_v2([10, 20, 15, 40, 21, 15, 35])

# multi mode
calculate_mode_v2([10, 20, 15, 20, 21, 15, 35])

# no-mode / all-mode
calculate_mode_v2([10, 20, 19, 23, 21, 15, 35])

# create numpy array
# calculate mean, mode and median using numpy functions
