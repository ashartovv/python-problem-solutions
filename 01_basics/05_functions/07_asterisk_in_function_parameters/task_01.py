# Input:
# A line containing names separated by spaces is given.
# Read the names and store them in the list writers.
#
# Define the function most_popular(people, *, case_sens=False).
# The function must return the first most frequently occurring name
# and its frequency as a tuple.
# If case_sens is True, letter case must be taken into account.
# Otherwise, letter case must be ignored.
#
# Test data:
#
# Input:
# Pushkin Lermontov Gogol Chekhov Krylov LERMONTOV Gogol CHEKHOV krylov Pushkin KRYLOV
#
# Output:
# No output
def most_popular(people, *, case_sens=False):
    popular_writer = ""
    count = 0

    if not case_sens:
        people = [writer.lower() for writer in people]

    for writer in people:
        if people.count(writer) > count:
            popular_writer = writer
            count = people.count(writer)

    return popular_writer, count


writers = input().split()
result = most_popular(writers, case_sens=True)