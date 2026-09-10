# Input:
# The program receives integers written separated by spaces.
# Read them and store them in a list.
#
# Then, sort this list in ascending order using the merge sort algorithm.
# The function must return a new sorted list.
#
# Call the resulting sorting function for the input list
# and display the result on the screen as a sequence of numbers
# separated by spaces.
#
# Hint:
# Use recursive functions to split the list and then assemble it.
#
# P.S. The sorting theory is covered in the video from the previous step.
#
# Test #1
# Input: 8 11 -6 3 0 1 1
# Output: -6 0 1 1 3 8 11

def merge_sorted(lst_1, lst_2):
    lst_sorted = []

    i = 0
    j = 0

    while i < len(lst_1) and j < len(lst_2):
        if lst_1[i] < lst_2[j]:
            lst_sorted.append(lst_1[i])
            i += 1

        elif lst_2[j] < lst_1[i]:
            lst_sorted.append(lst_2[j])
            j += 1

        else:
            lst_sorted.extend([lst_1[i], lst_2[j]])
            i += 1
            j += 1

    if i < len(lst_1) or j < len(lst_2):
        if i < len(lst_1):
            lst_sorted.extend(lst_1[i:])
        else:
            lst_sorted.extend(lst_2[j:])

    return lst_sorted


def sort_merge(lst):
    lst_1 = []
    lst_2 = []

    if len(lst) >= 2:
        lst_1 = sort_merge(lst[len(lst) // 2:])
        lst_2 = sort_merge(lst[:len(lst) // 2])
    else:
        return lst

    return merge_sorted(lst_1, lst_2)


N = list(map(int, input().split()))
print(*sort_merge(N))