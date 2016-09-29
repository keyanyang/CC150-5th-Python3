def compress(string):
    sl = []
    lastchar = ''
    charcount = 0
    for char in string:
        if char == lastchar:
            charcount += 1
        else:
            if lastchar == '':
                charcount = 1
            else:
                sl.append(lastchar + str(charcount))
                charcount = 1
            lastchar = char
    sl.append(char + str(charcount))
    sl = "".join(sl)

    if len(sl) < len(string):
        return sl
    else:
        return string
   
if __name__ == "__main__":
    print ("# 1.5")
    print(compress('abc'))
    print(compress('avvvbbbbcc'))
