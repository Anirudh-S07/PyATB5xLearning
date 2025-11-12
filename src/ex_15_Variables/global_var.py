count = 0
print(count)  # will print 0


def increment():
    global count
    count += 1  # will increase the count


increment()
increment()
increment()
increment()
increment()
print(count)  # will print 5


