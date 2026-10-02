numbers = [12, 7, 20, 15, 8, 3, 10, 5]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Numbers:", numbers)
print("Even numbers:", count)
