#search string if it is a or e or i or o or u then return count times
count = 0
s.lower()
for i in s:
    if i in ('a','e','i','o','u'):
        count += 1
print "Number of vowels:" + " " + str(count)
      