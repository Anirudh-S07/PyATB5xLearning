# Find the first non-repeating character in a string using sets
# swiss -> w is the answer

def first_non_repeating_sets(s):
    seen_once = set()
    seen_multiple = set()

    for ch in s:
        if ch in seen_multiple:
            continue
        elif ch in seen_once:
            seen_once.remove(ch)
            seen_multiple.add(ch)
        else:
            seen_once.add(ch)

    # Second pass: maintain order
    for ch in s:
        if ch in seen_once:
            return ch
    return None


print(first_non_repeating_sets("swiss"))  # w


# Without using sets
def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None
