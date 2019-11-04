def add(a, b):
    if type(a) is int or type(b) is int:
        print(a+b)
    else:
        print("argument type is invalid")


add(1, 2.1)
add("1", 2.1)


def age_check(age):
    print(f"you are {age}.")
    if age <= 12:
        print("Never!")
    elif age < 18 and age > 13:
        print("you can't drink.")
    elif age == 18 or age == 19:
        print("you are new to this.")
    else:
        print("Have a drink.")


age_check(12)
age_check(15)
age_check(19)
age_check(22)
