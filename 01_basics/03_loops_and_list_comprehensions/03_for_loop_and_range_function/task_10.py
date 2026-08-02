# Problem:
# A string containing city names separated by spaces is given as input.
#
# Read this string and create a list of city names.
#
# Using a for loop, check whether each next city name starts with
# the last letter of the previous city name.
#
# If the last letter is 'ь', 'ъ', or 'ы',
# use the previous letter instead.
#
# Output:
# "YES" if the entire sequence follows this rule,
# "NO" otherwise.
#
# Example:
#
# Input:
# Москва Астрахань Новгород Димитровград Душанбе
#
# Output:
# YES

cities = input().lower().split()
letters = ['ь', 'ъ', 'ы', ]
result = "YES"

for x in range(len(cities) - 1):
    if cities[x][-1] in letters:
        if cities[x][-2] != cities[x + 1][0]:
            result = "NO"
            break

    elif cities[x][-1] != cities[x + 1][0]:
        result = "NO"
        break

print(result)