from collections import deque
def solution(prices):
    prices_list = deque()
    total = []
    for i in range(len(prices)):
        count = 0
        for j in range( i + 1, len(prices)):
            if prices[i] <= prices[j]:
                count += 1
            else:
                pass
        prices_list.append(count)
    for q in prices_list:
        total.append(q)
    return total
p = input('쓰세요.:')
split_p = p.split()
for price in split_p:
    price = int(price)
    if price <1 or price > 10000:
        print('1이상 10000 이하의 자연수를 쓰세요.')
if len(split_p) < 2 or len(split_p) > 100000:
    print('길이를 2이상 100000이하로 쓰세요.')
else:
    print('prices\n',split_p)
    print('result\n',solution(split_p))