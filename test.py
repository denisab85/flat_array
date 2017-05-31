# ===================================================
#  Application name: flat_array test
#  Interpreter: Python 3.6
#  Description: functional tests for flat_array.py, uses test.txt for test cases
#  Version: 0.1
#  Date: 05/31/2017
#  Author: Denis Abakumov
# ===================================================

from flat_array import flatten
import ast
from collections import Counter


test_file = None
try:
    test_file = open("test.txt")
except:
    print ("Error opening file")

total_cnt = Counter({True: 0, False: 0})

if test_file:
    for line in test_file.readlines():
        test_array = []
        compare_array = []
        result_expected = None

        print(line.strip())

        if "==" in line:
            result_expected = True
            lines = line.split("==")
        elif "!=" in line:
            result_expected = False
            lines = line.split("!=")
        else:
            print("Error in expression")
            total_cnt['Skip'] += 1
            continue

        try:
            test_array = ast.literal_eval(lines[0].strip())
            compare_array = ast.literal_eval(lines[1].strip())
        except:
            print("Error in expression")
            total_cnt['Skip'] += 1
            continue
        test_array = flatten(test_array)
        result = ((test_array == compare_array) == result_expected)
        print(result)
        total_cnt[result] += 1
        print()
    print("============ totals ============")
    for cnt, num in total_cnt.items():
        print("{}: {}".format(cnt, num))
