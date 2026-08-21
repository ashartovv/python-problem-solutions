# Input:
# No direct input is required.
#
# Define the function are_anagrams(s1, s2, *, start=0, end=-1, ignore_case=True).
# It must check whether the parts of s1 and s2 in the range [start, end)
# are anagrams.
# Anagrams must contain the same characters with the same frequencies.
# If end == -1, process the strings to their ends.
# If ignore_case == True, letter case must be ignored.
# Otherwise, letter case must be considered.
# Return True if the selected parts are anagrams, otherwise return False.
#
# Call the function with words and ignore_case=False.
# Store the result in result.
#
# Test data:
#
# Input:
# No input.
#
# Output:
# No output.

def are_anagrams(s1, s2, *, start=0, end=-1, ignore_case=True):
    if ignore_case:
        s1 = s1.lower()
        s2 = s2.lower()

    d_s1 = {}
    d_s2 = {}

    for ch in set(s1[start:end]):
        d_s1[ch] = s1.count(ch)

    for ch in set(s2[start:end]):
        d_s2[ch] = s2.count(ch)

    return d_s1 == d_s2


words = input().split()

result = are_anagrams(*words, ignore_case=False)