marks = [78, 85, 67, 92, 74]
largest = marks[0]
for mark in marks:
    if mark > largest:
        largest = mark

print("Marks:", marks)
print("Largest mark:", largest)
