# right triangle start pattern

for i in range(5):
    for j in range(5):
        if j >= i+1:
            print("", sep="", end="")
        else:
            print("*", sep="", end="")
    print("", sep="")

