# Declare a generator function that yields prime numbers.
# A prime number is a natural number divisible only by 1 and itself.
# Generate the first 20 prime numbers, starting from 2.
# Print them on one line, separated by spaces.

def get_prime():
    count = 2
    yield count
    while True:
        count += 1
        is_even = True
        for i in range(2, count):
            if count % i == 0:
                is_even = False
                break

        if is_even:
            yield count

gen = get_prime()

for _ in range(20):
    print(next(gen), end=' ')