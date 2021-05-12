
"""Trying python conditions"""

NUMBER = 16
SECOND_NUMBER = False
first_array = [1, SECOND_NUMBER, 3]
second_array = [1, 1]

if NUMBER > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not SECOND_NUMBER:
    print("6")
