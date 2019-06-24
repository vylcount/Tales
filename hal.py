import os
import random
import time

resul = [{'name': "jon", 'age': 21},
         {'name': "mark", 'age': 45},
         {'name': "ed", 'age': 13}]


for dic in resul:
    keys = dic.keys()
    values = dic.values()
    items = dic.items()
    print(dic['name'])
    for key, value in dic.items():
        print(key, value)


# decorator to calculate duration
# # taken by any function.
# def calculate_time(hall):
#     # added arguments inside the inner1,
#     # if function takes any arguments,
#     # can be added like this.
#     def hall():
#         # storing time before function execution
#         begin = time.time()
#
#         for dic in resul:
#             keys = dic.keys()
#             values = dic.values()
#             items = dic.items()
#             # print(dic['name'])
#             print(list(items))
#
#         # storing time after function execution
#         end = time.time()
#         print("Total time taken in : ", hall.__name__, end - begin)
#
#     return hall
#
#
# calculate_time(hall)
