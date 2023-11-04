def number_burger(x):
    if x >= 100 and x <= 2000:
        burger.append(x)
    else:
        print('값을 다시 적어주세요.')
        x
def number_drink(y):
    if y >= 100 and y <= 2000:
        drink.append(y)
    else:
        print('값을 다시 적어주세요.')
        y

#f = lambda x, y : x + y -50

burger = []
drink = []

상덕버거 = int(input('상덕버거 입력:'))
number_burger(상덕버거)
중덕버거 = int(input('중덕버거 입력:'))
number_burger(중덕버거)
하덕버거 = int(input('하덕버거 입력:'))
number_burger(하덕버거)
콜라 = int(input('콜라 입력:'))
number_drink(콜라)
사이다 = int(input('사이다 입력:'))
number_drink(사이다)

#k = f(burger, drink)
total = [(i + j - 50) for i in burger for j in drink]

print(min(total))