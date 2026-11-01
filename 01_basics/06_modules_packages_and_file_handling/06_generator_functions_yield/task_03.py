# Read N and define a generator function that produces the first N numbers
# of the Balakirev sequence.
# Each number after the first three is the sum of the previous three numbers.
# The first three numbers are 1.
# Do not use collections.
# Call the generator N times and print the numbers on one line, separated by spaces.

def balak_seq(max_len):
    for _ in range(3):
        yield 1

    a, b, c = 1, 1, 1
    for _ in range(max_len - 3):
        a, b, c = b, c, a + b + c
        yield c


N = int(input())
gen = balak_seq(N)

for _ in range(N):
    print(next(gen), end=' ')