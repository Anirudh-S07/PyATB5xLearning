print(2+5)
print(x)  # Name error
# Exception is an event that occur during the execution of the program which disturbs the normal flow of instructions
#  A way to handle errors and unexpected situations gracefully
# Types of exceptions (Built-in)
"""
| Exception                | Meaning                              | When It Occurs                     | Example (raises the exception) |
| ------------------------ | ------------------------------------ | ---------------------------------- | ------------------------------ |
| **TypeError**            | Operation applied to wrong data type | Adding incompatible types          | `"5" + 1`                      |
| **ValueError**           | Correct type but invalid value       | Invalid conversion or argument     | `int("abc")`                   |
| **IndexError**           | Invalid list/tuple index             | Accessing out-of-range index       | `[1,2,3][5]`                   |
| **KeyError**             | Missing dictionary key               | Accessing key that doesn't exist   | `{"a":1}["b"]`                 |
| **AttributeError**       | Missing attribute/method             | Calling an attribute not on object | `(5).append(1)`                |
| **NameError**            | Name not defined                     | Using variable before declaring    | `print(x)`                     |
| **ZeroDivisionError**    | Division by zero                     | Mathematical operations            | `10 / 0`                       |
| **FileNotFoundError**    | File doesn’t exist                   | Opening a missing file             | `open("missing.txt")`          |
| **PermissionError**      | No permission to access resource     | Writing/reading protected file     | `open("/root/secret.txt")`     |
| **ModuleNotFoundError**  | Module not found                     | Importing a missing module         | `import abcxyz123`             |
| **ImportError**          | Import fails                         | Bad import syntax or location      | `from math import abc`         |
| **StopIteration**        | Iterator exhausted                   | Calling `next()` too many times    | `it = iter([]); next(it)`      |
| **RuntimeError**         | Generic runtime failure              | Illegal operations                 | `raise RuntimeError("fail")`   |
| **RecursionError**       | Max recursion depth reached          | Infinite recursion                 | `def f(): f(); f()`            |
| **OSError**              | General OS problem                   | Path issues / I/O issues           | `open("?:/badpath")`           |
| **TypeError (callable)** | Calling a non-callable object        | `obj()` on non-function            | `5()`                          |

"""

