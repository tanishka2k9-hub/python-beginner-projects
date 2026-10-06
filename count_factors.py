n=int(input("Enter the number:"))
count=0

for i in range(1,n+1):
    if  n%i==0:
        count+=1
print("The number of factors:",count)     
