n = int(input("Enter the number:"))
largest = 0

for i in range(1, n):
    if n % i == 0:
        if i > largest:
            largest = i

print("The largest factor:", largest)
