def name_can_be_anything():
    print("Main method")


def name_can_be_anything2():
    print("Main method2")


if __name__ == "__main__":  # Python Int -> Main method is -> Main Line
    name_can_be_anything()
    name_can_be_anything2()

"""
Here’s the clear, simple, but interview-level explanation of the main method and how it works in Python.

✅ What is a "main" method?

In many programming languages (Java, C, C++), the main method is the official entry point where the program starts.

Example in Java:

public static void main(String[] args) {
    System.out.println("Hello");
}


The program ALWAYS starts from main().

🤔 Does Python have a main method?

Python does NOT require a main() method.
But Python can use a main function, and it does have a standard entry-point mechanism:

if __name__ == "__main__":


This acts like Python’s version of a “main method”.

🧠 Why does Python not need a mandatory main()?

Because Python executes code from top to bottom, line by line.

Example:

print("Program started")


When you run this file → Python begins at the first line.

✅ The Python “main” pattern (Best practice)

Even though it’s optional, Python developers commonly add a main() function and call it like this:

def main():
    print("Hello from main")

if __name__ == "__main__":
    main()

🔍 What does if __name__ == "__main__": mean?

Every Python file has a built-in variable named __name__.

Two cases:

1. When you run the file directly:
python myfile.py


Then:

__name__ == "__main__"


So Python executes the code inside that block.

2. When the file is imported into another file:
import myfile


Then:

__name__ == "myfile"


So Python does NOT run the main() block during import.

👉 Why is this useful?
✔ Prevents code from running accidentally when importing

If you have automation scripts, test utilities, helper modules, etc., 
you don’t want the script to execute automatically just because it was imported.

Example:

utils.py

def add(a, b):
    return a + b

def main():
    print(add(2, 3))

if __name__ == "__main__":
    main()


Now:

import utils


Does NOT print anything — safe.

But:

python utils.py


Prints 5.

🧪 SDET / Automation relevance

You will use it in:

PyTest utilities

Custom Python libraries

Test helpers

Running scripts only when executed, not imported

Example for framework:

def run_tests():
    print("Running all automation tests...")

if __name__ == "__main__":
    run_tests()

🎯 Interview-ready explanation (Use this)

Q: Does Python have a main method?

Python does not require a main() method like Java or C, 
but we often define a main() function and call it inside if __name__ == "__main__": to indicate the entry point of the script. 
This ensures the code only runs when the file is executed directly, and not when it is imported as a module.

"""
