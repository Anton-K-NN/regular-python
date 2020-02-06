'''
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.
Sample Input:

this is a text
"this' !is. ?n1ce,
Sample Output:

htis si a etxt
"htis' !si. ?1nce,
'''
import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern=r"\b(a|A)([a|A])+(a|A)\b"
    match_obj=re.sub(pattern, "argh", line, count=1)
    if match_obj:
        print(match_obj)