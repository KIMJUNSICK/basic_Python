def p_add(a, b):
    print(a + b)


def r_add(a, b):
    return a+b
    print("asdasdasd")  # not work. because 'return' terminated Ftn


r_value = r_add(1, 2)
p_value = p_add(1, 2)

print(r_value, p_value)  # 3, None
