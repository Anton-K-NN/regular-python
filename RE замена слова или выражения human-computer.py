'''
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".

Примечание:
Обратите внимание на параметр count у функции sub.
Sample Input:

There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA
Sample Output:

There’ll be no more "argh"
argh AaAaAaA
'''
import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern=r"a"
    match_obj=re.sub(pattern,"argh", line)
    if match_obj:
        print(match_obj)