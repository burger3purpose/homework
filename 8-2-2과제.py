def number(x):
    if x <= 1000 and type(x) is int:
        x%42
        total.append(x)
    else:
        print('다시 입력해')
        x

total = []

def number(x):
    if x <= 1000 and type(x) is int:
        remainder = x % 42
        total.append(remainder)

[ number(int(input(f'{i+1}번째 수 입력:')) ) for i in range(10) ]

total = list(set(total))

print(len(total))
