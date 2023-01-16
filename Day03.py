num = int(input("Enter a number(0 to quit) : "))
counts = 0

k=1
while k<= num:
    if num % k == 0:
        counts += 1
    k += 1
if counts == 2:
    print(f"{num} is prime number!")
else:
    print(f"{num} is Not prime number")

