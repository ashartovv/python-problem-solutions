# Declare the following list of city names:
# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# Create a generator that uses this list to yield 1,000,000 city names in a loop.
# After reaching the end of the list, return to the beginning and repeat the iteration.
# Print the first 20 city names generated, on a single line separated by spaces.

cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]

gen = (x for x in cities * 1000000)

for _ in range(20):
    print(next(gen), end=' ')