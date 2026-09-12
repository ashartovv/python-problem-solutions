# Input:
# The program receives a string in the following format:
# key_1=value_1 key_2=value_2 ... key_N=value_N
#
# Read the string from the input.
#
# Using the map() function, convert the string into a tuple named tp
# with the following structure:
#
# tp = (('key_1', 'value_1'), ('key_2', 'value_2'), ..., ('key_N', 'value_N'))
#
# Do not display anything on the screen.
# Only create the tuple named tp.
#
# Input:
# house=home car=vehicle men=person tree=plant

s = input()
s_lst = s.split()

tp = tuple(map(tuple, map(lambda s: s.split('='), s_lst)))