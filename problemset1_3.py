#find the longest string that is in alphabetical order 

s = 'abcca'
lst = [0]
count = 0
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        count += 1
        lst.append(count)
    else:
        count = 0
        lst.append(count)
location = lst.index(max(lst))
large = max(lst)
print 'Longest substring in alphabetical order is:' + ' ' +  str(s[location - large : location + 1])
    

