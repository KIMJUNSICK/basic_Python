def add(a, b):
    if type(a) is int or type(b) is int:
        print(a+b)
    else:
        print("argument type is invalid")


add(1, 2.1)
add("1", 2.1)
