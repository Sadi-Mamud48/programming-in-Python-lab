total = 0

for i in range(2, 1000):
    prime = True
    for num in range(2, i):
        if i % num == 0:
            prime = False
            break
    if prime:
        total = total + i

print("Sum of prime numbers:", total)