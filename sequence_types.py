# sequrence type - list & tuple
# list is mutable
# tuple is immutable

# list - []
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

print(type(days))  # list

# list operation - in
print("Mon" in days)  # True
print("MON" in days)  # False

# list operation - len
print(len(days))

# list operation - reverse
days.reverse()
print(days)

# list operation - clear
days.clear()
print(days)

# list operation - append
days.append("Sat")
print(days)

# find data in list with order infomation
print(days[0])  # Thu

# tuple - ()
days2 = ("Mon", "Tue", "Wed", "Thu", "Fri")

print(type(days2))  # tuple
