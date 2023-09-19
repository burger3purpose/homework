import re

def extract_emails(text):
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    email_addresses = re.findall(pattern, text)
    return email_addresses

text = input('텍스트를 입력하세요: ')

email_list = extract_emails(text)

if email_list:
    for email in email_list:
        print(email)
else:
    print('이메일 주소가 발견되지 않았습니다.')