# Problem:
# The following data is given as input, each on a separate line:
# - dollar exchange rate (floating-point number);
# - amount of rubles (integer) to exchange for dollars.
#
# Read these values and calculate the whole number of dollars received
# (discarding the fractional part).
# Create a string using the following template:
#
# "You can get <dollars>$ for <rubles> rubles at the exchange rate <dollar rate>"
#
# Display the resulting string without quotation marks.
#
# Input:
# The dollar exchange rate and the amount of rubles,
# each on a separate line.
#
# Output:
# A formatted currency exchange message.
#
# Example:
# Input:
# 92.5
# 1000
#
# Output:
# You can get 10$ for 1000 rubles at the exchange rate 92.5

dollar_rate = float(input())
ruble_count = int(input())

print(f"You can get {int(ruble_count / dollar_course)}$ for {ruble_count} rubles at the exchange rate {dollar_course}")