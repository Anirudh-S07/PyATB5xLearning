# Length of set
setp = set(["The TestingAcademy", "asdasdad","thetestingacademy"])
print(setp)
print(len(setp))

# Iteration through set
for i in setp:
    print(i)

# asdasdad
# thetestingacademy
# The TestingAcademy

setp.add("Pramod")
print(setp)
setp.add("Pramod")
print(setp)

"""

| Function / Method | Description                                               | Example            |
| ----------------- | --------------------------------------------------------- | ------------------ |
| `add()`           | Adds a single element                                     | `s.add(4)`         |
| `update()`        | Adds multiple elements (from list, tuple, set, etc.)      | `s.update([5, 6])` |
| `remove()`        | Removes an element, raises error if not found             | `s.remove(3)`      |
| `discard()`       | Removes an element, does **not** raise error if not found | `s.discard(10)`    |
| `pop()`           | Removes and returns an arbitrary element                  | `s.pop()`          |
| `clear()`         | Removes all elements                                      | `s.clear()`        |
| `copy()`          | Returns a shallow copy                                    | `t = s.copy()`     |

"""