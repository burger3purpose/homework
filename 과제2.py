def total_num(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + total_num(nums[1:])

start = input('Enter integers separated by spaces: ')
if start == 'done':
    print('Program terminated. Goodbye!')
    exit()
second = start.split()
third = []

try:
    for x in second:
        third.append(int(x))
    print('The sum of the input integers is', total_num(third))
except ValueError:
    print('You must enter integers separated by spaces.')