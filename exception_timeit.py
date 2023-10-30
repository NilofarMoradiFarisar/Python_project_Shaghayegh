from timeit import timeit

code = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10/age


try:
    calculate_xfactor(-1)
except BaseException as ex:
    # print(ex)
    pass
"""
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age



xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""


print("code_first", timeit(code, number=100))
print("code_finall", timeit(code1, number=100))
