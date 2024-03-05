from z3 import *
import re
import math
from Cryptodome.Util.number import *


def count(x, target):
    count = 0
    for i in range(len(x)):
        if x[i] == target:
            count += 1
    return count


def sumdigit(x):
    sum = 0
    for i in range(len(x)):
        if x[i] == '1':
            sum += 1
        if x[i] == '2':
            sum += 2
        if x[i] == '3':
            sum += 3
        if x[i] == '4':
            sum += 4
        if x[i] == '5':
            sum += 5
        if x[i] == '6':
            sum += 6
        if x[i] == '7':
            sum += 7
        if x[i] == '8':
            sum += 8
        if x[i] == '9':
            sum += 9
    return sum


def lentarget(x):
    count = 0
    for i in range(len(x)):
        if x[i] == '1' or x[i] == '2' or x[i] == '3' or x[i] == '4' or x[i] == '5' or x[i] == '6' or x[i] == '7' or x[i] == '8' or x[i] == '9' or x[i] == '0':
            count += 1
    return count


def matchSub(x, target):
    for i in range(len(x)-4):
        if x[i:i+4] == target:
            return True
    return False


def Distinct(x):
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            return True
    return False


def countDistinct(x):
    distinctList = []
    for i in range(len(x)):
        if x[i] not in distinctList:
            distinctList.append(x[i])
    return len(distinctList)


def countAsciiMatch(x):
    sum = 0
    for i in x:
        sum += ord(i)
    sum %= 65
    if sum == 0:
        return True
    else:
        return False


def countHex(x):
    hexv = ["0", "1", "2", "3", "4", "5", "6", "7",
            "8", "9", "a", "b", "c", "d", "e", "f"]
    count = 0
    for i in x:
        if i in hexv:
            count += 1
    return count


def countVowel(x):
    vowel = ["a", "e", "o", "i", "u"]
    for i in x:
        if i in vowel:
            vowel.remove(i)
    return 5 - len(vowel)


s = z3.Solver()

x = ""

s.add(type(x) == "<class 'str'>")
s.add(len(x) >= 6)
s.add(x[0:8] == "hkcert23{")
s.add(count(x, '1')*3 == count(x, '6'))
s.add(count(x, '5') == 5)
s.add(count(x, '{') == 1)
s.add(count(x, '}') == 1)
s.add(isPrime(len(x)) == True)
s.add(sumdigit(x) == 26)
s.add(len(x) <= 42)
s.add(count(x, '_') >= 3)
s.add(matchSub(x, 'flag') == False)
s.add(isPrime(lentarget(x)) == True)
s.add(lentarget(x) <= len(x)*0.3)
s.add(matchSub(x, 'fail') == False)
s.add(matchSub(x, 'y0u') == True)
s.add(Distinct(x) == False)
s.add(countDistinct(x) == 20)
s.add(countAsciiMatch(x) == True)
s.add(countHex(x) >= len(x) * 0.4)
s.add(countVowel(x) <= 2)


print(s.check())

# sum = 0


# lll = "hkcert23{my0uztgj3131d6d1d3d3_d_g_d_}"
# lll = list(lll)
# for i in lll:
#     sum += ord(i)

# print(sum % 65)

# print(chr(ord('j')-5))
# print(ord('@'))
# print(ord('3'))
