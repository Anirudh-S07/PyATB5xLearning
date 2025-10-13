
def make_sandwich(*args, default="butter only"):
    sandwich_sentence = "Sandwich prepared with "
    if not args:
        return sandwich_sentence + default + "."
    else:
        return sandwich_sentence + ", ".join(args)+"."


print(make_sandwich("tomato", "keera", "gongura"))
print(make_sandwich())
