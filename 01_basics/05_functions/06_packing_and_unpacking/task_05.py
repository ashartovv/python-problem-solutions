# Input:
# Additional menu items are given as strings in the format:
# name_1=url_1
# ...
# name_N=url_N
#
# Convert the list lst_in into a dictionary and add its items
# to the existing dictionary menu using dictionary unpacking.
# The resulting dictionary must be stored in the variable menu.
#
# Nothing should be printed.
#
# Test data:
#
# Input:
# Cities=about-cities
# Cars=read-of-cars
# Airplanes=airplanes
#
# Output:
# No output

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
d = { row.split("=")[0]: row.split("=")[1]
     for row in lst_in
      }

menu = {**menu, **d}