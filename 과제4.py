import re

with open("C:/Users/sam03/OneDrive/바탕 화면/2학기 프로그래밍/mbox.txt", 'r') as file:
    content = file.read()
pattern = r'\(New Revision : (\d+)\)'
numbers = re.findall(pattern, content)
numbers = [int(num) for num in numbers]
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"평균값: {average:.2f}")
else:
    print("숫자를 찾을 수 없습니다.")