public_toilet = "PB"


def home():
    private_toilet = "PT"
    print(private_toilet)
    public_toilet = "LPB"  # this has more preference that is it will change the variable
    print(public_toilet)


home()  # output is PT and LPB
