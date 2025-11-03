def outer_function():
    var1 = 30  # local variable for outer_function()

    def inner_function():
        print(var1)  # For inner_function() var1 is global variable
        var2 = 78

    def inner_function2():
        print(var1)  # For inner_function2() var1 is global variable
      # print(var2)  # Not possible as it is variable of inner_function() will give Unresolved reference 'var2'

    inner_function()
    inner_function2()
  # print(var2)  # Not possible as it is variable of inner_function() will give Unresolved reference 'var2'


outer_function()
# inner_function() is not possible
