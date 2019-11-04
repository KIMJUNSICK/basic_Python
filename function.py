# Built-in-function
print("junsik")  # junsik
print(len("Asdasdd"))  # 7

age = "18"
print(age)
print(type(age))

new_age = int(age)
print(new_age)
print(type(new_age))


# Custom function
def call_name(name="anonymous"):
    print("Hello", name)


call_name()
call_name("junsik")


def add(a, b):
    print(a+b)


add(1, 2)
# add(1) =>  # arguments called 'b' is needed => add(a, b=0)


def add2(a, b=0):
    print(a+b)


add2(1, 2)  # 3
add2(1)  # 1
