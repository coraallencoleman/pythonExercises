
#find number of "bob"s in s

s = 'obobobobbooboboboobob'

result = 0

for i, letter in enumerate(s):
    if i == len(s)-2:
        break
    else:
        guess = s.count('bob', i, i+3)
        if guess > 0:
            result += guess
print "Number of times bob occurs is: {}".format(result)