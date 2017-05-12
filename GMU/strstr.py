#Tail Recursion
def strstrTail(s, pattern, index):
    if len(s) < len(pattern):
        return -1
    print("{0}: {1}".format(index, s))
    if pattern == s[0:len(pattern)]:
        return index
    else:
        return strstrTail(s[1:], pattern, index+1)

def strstr(s, pattern):
    index = 0
    return strstrTail(s, pattern, index)
