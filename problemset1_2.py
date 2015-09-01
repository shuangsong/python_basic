#search a string and count how many times a word occur in it:
s = 'voboboobobeboboboopcoboboboboboow'
sb = 'bob'
results = 0
sub_len = len(sb)
for i in range(len(s)):
    if s[i:i+sub_len] == sb:
        results += 1
print "Number of times bob occurs is:" + " " + str(results)
      