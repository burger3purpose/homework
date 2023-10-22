from collections import Counter
file1 = open("C:/Users/sam03/OneDrive/바탕 화면/새 폴더/06 file01.txt",'r')
file2 = open("C:/Users/sam03/OneDrive/바탕 화면/새 폴더/06 file02.txt",'r')
file1_list = file1.read().split()
file2_list = file2.read().split()
for i in range(len(file1_list)):
    if '.' in file1_list[i]:
        file1_list[i] = file1_list[i].replace('.','')
    file1_list[i].lower()
for i in range(len(file2_list)):
    if '.' in file2_list[i]:
        file2_list[i] = file2_list[i].replace('.','')
    file2_list[i].lower()
counter1 = Counter(file1_list)
counter2 = Counter(file2_list)
result = counter1 & counter2
print(counter1,counter2)

print('공통된 단어와 각 파일에서의 빈도:')
for word in result:
    print('{0}:파일1-{1}/파일2-{2}'.format(word, counter1[word],counter2[word]))