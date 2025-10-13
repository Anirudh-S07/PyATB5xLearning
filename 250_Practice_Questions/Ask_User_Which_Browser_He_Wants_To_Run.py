# Write a program to ask the user which browser he wants to run automation.

browser_name = input("Enter the browser Name\n")
match browser_name:
    case "firefox":
        print("Starting FireFox")
    case "chrome":
        print("Starting Chrome")
    case "edge":
        print("Starting Edge")
    case "safari":
        print("Starting Safari")
    case _:  # default
        print("Browser Not found!")
