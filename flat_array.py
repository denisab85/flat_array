# ===================================================
#  Application name: flat_array
#  Interpreter: Python 3.6
#  Description: flattens an array of arbitrarily nested arrays of integers into a flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4]
#  Version: 0.1
#  Date: 05/31/2017
#  Author: Denis Abakumov
# ===================================================


def flatten(array):
    result = []
    for a in array:
        if isinstance(a, list):
            result.extend(flatten(a))
        else:
            result.append(a)
    return result
