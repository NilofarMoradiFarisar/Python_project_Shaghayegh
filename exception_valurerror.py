# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less")
#     return 10/age


# print(calculate_xfactor(-1))


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10/age


try:
    calculate_xfactor(-1)
except OverflowError as ex:
    print(ex)
