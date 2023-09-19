def rev_str(str):
    if len(str) <= 1:
        return str
    else:
        result_str = rev_str(str[1:])
        return result_str + str[0]
print(rev_str('ABCDE'))
print(rev_str('Come again, Forever young!'))
print(rev_str('Amore, Roma'))