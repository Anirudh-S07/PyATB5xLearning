pb_global_b = 12  # Global Variable outside of Function


def my_func():
    pb_a = 10  # Local Variable within function
    print(pb_a)
    print(pb_global_b)


# print(pb_a) not possible will give
print(pb_global_b)
my_func()
