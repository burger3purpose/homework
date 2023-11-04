from collections import deque
string = list('This is a more advanced comprehension exercise to practice')
string.reverse()
string = ''.join(string)
string = string.split()
string = deque(reversed(string))
print(string)
x = [i for i in string if len(i) >= 5]
print(x)
