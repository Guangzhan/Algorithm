def firstOccurOnceChar(s):
    l = len(s)
    h = [0] * 256
    for i in xrange(l):
        h[ord(s[i])] += 1
    rslt = ''
    for i in xrange(l):
        if h[ord(s[i])] == 1:
            rslt = s[i]
            break
    return rslt
