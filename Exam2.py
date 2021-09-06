words = input().split()
print(len(set(words)), end=' ')
for i in set(words):
    print(words.count(i), end = '')


'''
words = input().split()
words_count = {}

for w in words:
    words_count[w] = words_count.get(w,0) + 1
print(len(words_count), end = ' ')
for freq in words_count.keys():
    print(words_count[freq], end= '')
'''
words = input().split()
unique_words = set(words)
print(len(unique_words), end=' ')
for i in unique_words:
    print(words.count(i), end = '')
