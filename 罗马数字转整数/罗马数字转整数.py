adict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
           'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
alist = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
s += ' '
res, i = 0, 0
while i < len(s)-1:
    if s[i]+s[i+1] in alist:
        res += adict[s[i]+s[i+1]]
        i += 2
    else:
        res += adict[s[i]]
        i += 1
return res
