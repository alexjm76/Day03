num = int(input("Enter a number(0 to quit) : "))
is_prime =True

k = 1

for k in range(2, num):
    if num % k == 0:
        is_prime = False
if is_prime:
    print(f"{num} is prime number!")
else:
    print(f"{num} is Not prime number")