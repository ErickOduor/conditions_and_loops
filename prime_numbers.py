#program to find prime numbers between two numbers 

primes = []
lower_bound = int(input("Enter the lower integer: ")) 
upper_bound = int(input("Enter the upper integer: ")) 
 
for num in range(lower_bound, upper_bound):
    is_prime = True 
    for prime in range(2, num):
        if num % prime == 0:
            is_prime = False
            break 
    if is_prime: 
        primes.append(num)

print('primes from ',str(lower_bound),' up to ' + str(upper_bound) + ': ' + str(primes))
print('There are ', str(len(primes)), ' prime numbers in the range')