# Problem:
# The following address information is given as input,
# each on a separate line:
# - city (string);
# - street (string);
# - house number (integer);
# - apartment number (integer).
# Read the input and create the following string using an f-string:
#
# "City: <city>, Street: <street>, House: <house number>, Apartment: <apartment number>"
#
# Display the resulting string without quotation marks.
#
# Input:
# The city, street, house number, and apartment number,
# each on a separate line.
#
# Output:
# A formatted address string.
#
# Example:
# Input:
# New York
# Broadway
# 15
# 42
#
# Output:
# City: New York, Street: Broadway, House: 15, Apartment: 42

city = str(input())
street = str(input())
house_number = int(input())
apartment_number = int(input())

print(f"City: {city}, Street: {street}, House: {house_number}, Apartment: {apartment_number}")