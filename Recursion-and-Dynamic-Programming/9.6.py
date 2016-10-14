def parentheses(left, right, list):
    if left < 0 or left > right:
        return
    if left == 0 and right == 0:
        for i in list:
            print(i, end='')
        print('')
    else:
        parentheses(left - 1, right, list + ['('])
        parentheses(left, right - 1, list + [')'])

def pt1(counter):
    return parentheses(counter, counter, [])        

pt1(3)
