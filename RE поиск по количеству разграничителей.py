'''
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
Sample Input:

zabcz
zzz
zzxzz
zz
zxz
zzxzxxz
Sample Output:

zabcz
zzxzz
'''
import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern=r"z.{3}z"
    match_obj=re.search(pattern,line)
    if match_obj:
        print(line)