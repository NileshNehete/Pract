#import constant

#print (constant.PI)

str = 'I|%am|^Nilesh|*Nehete'

# 2 is maxsplit items.

print ( str.split('|',2))

# if nothing is mentioned then complete items are comsidered.

print ( str.split('|'))

temp = 0

while ( temp < 10 ):
    print temp
    if (temp == 5):
        break
    temp += 1


