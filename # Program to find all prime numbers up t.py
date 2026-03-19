2# Program to find all prime numbers up to a given limit (max 100)
# It also calculates:
# - Total count of primes
# - Smallest prime
# - Largest prime
# - Sum of all primes

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Efficient check up to sqrt(num)
        if num % i == 0:
            return False
    return True

# Taking user input
limit = int(input("Enter a number (max 100): "))

# Validate input
if limit > 100 or limit < 1:
    print("Please enter a number between 1 and 100.")
else:
    primes = []  # List to store prime numbers

    # Find all prime numbers up to the limit
    for number in range(1, limit + 1):
        if is_prime(number):
            primes.append(number)

    # Display results
    print("\nPrime numbers found:", end=" ")
    for p in primes:
        print(p, end=" ")

    # Calculations
    total_primes = len(primes)
    sum_primes = sum(primes)

    if total_primes > 0:
        smallest = primes[0]
        largest = primes[-1]
    else:
        smallest = None
        largest = None

    # Output statistics
    print("\nTotal primes found:", total_primes)
    print("Largest prime:", largest)
    print("Smallest prime:", smallest)
    print("Sum of all primes:", sum_primes)