for n in range(10):
    if n % 2 == 0:
        continue
    else:
        print(n)

# Three table formula
# |i | Condition | O/P
# |0 | 0%2 == 0 -> True | O/P = continue - skip this step go to next
# |0 | 1 == 1%2 -> False | O/P = 1
# |0 | 2 == 2%2 -> True | O/P = continue - skip this step go to next
# |0 | 3 == 3%2 -> False | O/P = 3
# |0 | 4 == 4%2 -> True | O/P = continue - skip this step go to next
# |0 | 5 == 5%2 -> False | O/P = 5
# |0 | 6 == 6%2 -> True | O/P = continue - skip this step go to next
# |0 | 7 == 7%2 -> False | O/P = 7
# |0 | 8 == 8%2 -> True | O/P = continue - skip this step go to next
# |0 | 9 == 9%2 -> False | O/P = 9
# |0 | 10 == 10%2 -> True | O/P = Exit as the last is 10-1

# Difference between pass and continue is pass can also be used in statement, functions, classes and objects.
