# Built-In -Functions
# Pre defined given by the Python guys for you to use it

# max()
# min()
# print()

"""

| **Function**     | **Description**                  | **Example**                            |
| ---------------- | -------------------------------- | -------------------------------------- |
| `abs()`          | Returns absolute value           | `abs(-7) → 7`                          |
| `all()`          | True if all items are true       | `all([1, True, 3]) → True`             |
| `any()`          | True if any item is true         | `any([0, False, 5]) → True`            |
| `ascii()`        | Returns printable representation | `ascii('ä') → '\\xe4'`                 |
| `bin()`          | Converts to binary string        | `bin(5) → '0b101'`                     |
| `bool()`         | Converts to Boolean              | `bool([]) → False`                     |
| `breakpoint()`   | Enters debugger                  | `breakpoint()`                         |
| `bytearray()`    | Creates mutable byte array       | `bytearray("Hi", "utf-8")`             |
| `bytes()`        | Creates immutable bytes          | `bytes("Hi", "utf-8")`                 |
| `callable()`     | Checks if object is callable     | `callable(len) → True`                 |
| `chr()`          | Returns character from ASCII     | `chr(65) → 'A'`                        |
| `classmethod()`  | Converts to class method         | `classmethod(func)`                    |
| `compile()`      | Compiles source to code object   | `compile('2+3', '', 'eval')`           |
| `complex()`      | Creates complex number           | `complex(2, 3) → (2+3j)`               |
| `delattr()`      | Deletes object attribute         | `delattr(obj, 'attr')`                 |
| `dict()`         | Creates dictionary               | `dict(a=1, b=2)`                       |
| `dir()`          | Lists attributes/methods         | `dir([])`                              |
| `divmod()`       | Returns (quotient, remainder)    | `divmod(5, 2) → (2, 1)`                |
| `enumerate()`    | Adds counter to iterable         | `list(enumerate(['a','b']))`           |
| `eval()`         | Evaluates a string expression    | `eval("2 + 3") → 5`                    |
| `exec()`         | Executes Python code             | `exec("x=5; print(x)")`                |
| `filter()`       | Filters items by function        | `list(filter(lambda x: x>2, [1,2,3]))` |
| `float()`        | Converts to float                | `float('3.5') → 3.5`                   |
| `format()`       | Returns formatted string         | `"{} {}".format('Hi',5)`               |
| `frozenset()`    | Immutable set                    | `frozenset([1,2,3])`                   |
| `getattr()`      | Gets attribute value             | `getattr(obj, 'name')`                 |
| `globals()`      | Returns global namespace dict    | `globals()`                            |
| `hasattr()`      | Checks if object has attribute   | `hasattr(obj, 'attr')`                 |
| `hash()`         | Returns hash value               | `hash('Hi')`                           |
| `help()`         | Displays help                    | `help(str)`                            |
| `hex()`          | Converts to hex string           | `hex(255) → '0xff'`                    |
| `id()`           | Returns unique object ID         | `id(5)`                                |
| `input()`        | Reads user input                 | `input("Name: ")`                      |
| `int()`          | Converts to integer              | `int('10') → 10`                       |
| `isinstance()`   | Checks object type               | `isinstance(5, int) → True`            |
| `issubclass()`   | Checks subclass relation         | `issubclass(bool, int)`                |
| `iter()`         | Returns iterator object          | `iter([1,2,3])`                        |
| `len()`          | Returns length                   | `len("abc") → 3`                       |
| `list()`         | Creates list                     | `list((1,2,3)) → [1,2,3]`              |
| `locals()`       | Returns local variables dict     | `locals()`                             |
| `map()`          | Applies function to iterable     | `list(map(str, [1,2,3]))`              |
| `max()`          | Returns maximum value            | `max([1,5,3]) → 5`                     |
| `memoryview()`   | Creates memory view              | `memoryview(b'abc')`                   |
| `min()`          | Returns minimum value            | `min([1,5,3]) → 1`                     |
| `next()`         | Returns next item from iterator  | `next(iter([10,20])) → 10`             |
| `object()`       | Creates new base object          | `object()`                             |
| `oct()`          | Converts to octal string         | `oct(8) → '0o10'`                      |
| `open()`         | Opens a file                     | `open('file.txt')`                     |
| `ord()`          | Returns Unicode code point       | `ord('A') → 65`                        |
| `pow()`          | Raises to power (xⁿ)             | `pow(2,3) → 8`                         |
| `print()`        | Prints to console                | `print("Hello")`                       |
| `property()`     | Creates managed attribute        | `property(get_func, set_func)`         |
| `range()`        | Returns sequence of numbers      | `range(5) → 0,1,2,3,4`                 |
| `repr()`         | Returns string representation    | `repr(5) → '5'`                        |
| `reversed()`     | Reverses iterable                | `list(reversed([1,2,3]))`              |
| `round()`        | Rounds number                    | `round(3.6) → 4`                       |
| `set()`          | Creates set                      | `set([1,2,2]) → {1,2}`                 |
| `setattr()`      | Sets attribute value             | `setattr(obj, 'attr', 5)`              |
| `slice()`        | Creates slice object             | `slice(1,5)`                           |
| `sorted()`       | Returns sorted list              | `sorted([3,1,2]) → [1,2,3]`            |
| `staticmethod()` | Converts to static method        | `staticmethod(func)`                   |
| `str()`          | Converts to string               | `str(123) → '123'`                     |
| `sum()`          | Sums iterable items              | `sum([1,2,3]) → 6`                     |
| `super()`        | Access parent class              | `super().method()`                     |
| `tuple()`        | Creates tuple                    | `tuple([1,2]) → (1,2)`                 |
| `type()`         | Returns object type              | `type(5) → <class 'int'>`              |
| `vars()`         | Returns object’s **dict**        | `vars(obj)`                            |
| `zip()`          | Combines iterables into tuples   | `list(zip([1,2],[3,4]))`               |
| `__import__()`   | Imports module dynamically       | `__import__('math')`                   |


"""

print(pow(2, 3))
b = abs(-10)  # Return the absolute value of the argument
print(b)


# User defined functions

# Part-1 -Define
def greet():
    print("Hello, Welcome")


# Part-2 Call
greet()
