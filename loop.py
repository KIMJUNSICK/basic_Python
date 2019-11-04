days = ("Mon", "Tue", "Wed", "Thu", "Fri")

# same result
# It has nothing to do with name that after 'for'.
for x in days:
    print(x)

for tomato in days:
    print(tomato)

for day in days:
    print(day)

# method that break loop
for day in days:
    if day is "Wed":
        break
    else:
        print(day)

# string
for letter in "junsik":
    print(letter)
