str1 = input('Enter string 1 :  ')
str2 = input('Enter string 2 :  ')
count1 = 0
count2 = 0
for i in str1:
    count1 += ord(i)
for i in str2:
    count2 += ord(i)
if count1 == count2:
    print('These are Anagrams.')
else:
    print('These are not Anagrams.')


# Alternate way
"""
str1 = input('Enter string 1 :  ')
str2 = input('Enter string 2 :  ')
if sorted(str1) == sorted(str2):
    print('These are Anagrams.')
else:
    print('These are not Anagrams.')
"""