var1 = 1000
var2 = 1000
var3 = 999
print("first_var =", var1, ", address is", id(var1))
print("second_var =", var2, ", address is", id(var2))
print("third_var =", var3, ", address is", id(var3))
if var1 == var2 :
    print(var1, "is", var2, "=", True)
if var1 != var3 :
    print(var1, "is", var3, "=", False)