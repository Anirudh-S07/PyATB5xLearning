# pass
for i in range(0, 10, 1):
    if i == 5 or i == 6:
        print(i)
    else:
        pass  # pass is a placeholder where in it does nothing


# Three table formula
# |i | Condition | O/P
# |0 | 0 == 5 -> False | O/P = Nothing
# |0 | 1 == 5 -> False | O/P = Nothing
# |0 | 2 == 5 -> False | O/P = Nothing
# |0 | 3 == 5 -> False | O/P = Nothing
# |0 | 4 == 5 -> False | O/P = Nothing
# |0 | 5 == 5 -> True | O/P = 5
# |0 | 6 == 6 -> True | O/P = 6
# |0 | 7 == 5 -> False | O/P = Nothing
# |0 | 8 == 5 -> False | O/P = Nothing
# |0 | 9 == 5 -> False | O/P = Nothing
# |0 | 10 == 5 -> False | O/P = Exit as the last is 10-1

# break
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


