for i in range(0, 10):
    if i == 5:
        print("Five")
    else:
        print(i)

# Three table formula
# |i | Condition | O/P
# |0 | 0 == 5 -> False | O/P = 0
# |0 | 1 == 5 -> False | O/P = 1
# |0 | 2 == 5 -> False | O/P = 2
# |0 | 3 == 5 -> False | O/P = 3
# |0 | 4 == 5 -> False | O/P = 4
# |0 | 5 == 5 -> True | O/P = "Five"
# |0 | 6 == 5 -> False | O/P = 6
# |0 | 7 == 5 -> False | O/P = 7
# |0 | 8 == 5 -> False | O/P = 8
# |0 | 9 == 5 -> False | O/P = 9
# |0 | 10 == 5 -> False | O/P = Exit as the last is 10-1

for i in range(0, 10):
    if i == 5:
        break
    else:
        print(i)

# Three table formula
# |i | Condition | O/P
# |0 | 0 == 5 -> False | O/P = 0
# |0 | 1 == 5 -> False | O/P = 1
# |0 | 2 == 5 -> False | O/P = 2
# |0 | 3 == 5 -> False | O/P = 3
# |0 | 4 == 5 -> False | O/P = 4
# |0 | 5 == 5 -> True | O/P = Exit as the condition is satisfied

for i in range(0, 6, 1):
    if i == 5:
        print(i)
    else:
        print("No O/P")

# Three table formula
# |i | Condition | O/P
# |0 | 0 == 5 -> False | O/P = "No O/P"
# |0 | 1 == 5 -> False | O/P = "No O/P"
# |0 | 2 == 5 -> False | O/P = "No O/P"
# |0 | 3 == 5 -> False | O/P = "No O/P"
# |0 | 4 == 5 -> False | O/P = "No O/P"
# |0 | 5 == 5 -> True | O/P = 5



