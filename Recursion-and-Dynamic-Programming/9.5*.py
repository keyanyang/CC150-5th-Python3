def permutation(str):
    if str == '': return ['']
    result = []
    for i in range(len(str)):
        rest = permutation(str[:i] + str[i+1:])
        for n in rest:
            result.append(str[i] + n)
    return result
        

per = permutation('asd')
print(per)
print('the number of permutation is:')
print(len(per))
