# Reverse Triangle Pattern

for i in range(5):
    for j in range(5):
        if j < 5-i:
            print("*", sep="", end="")
        else:
            print("", sep="", end="")
    print("", sep="")
