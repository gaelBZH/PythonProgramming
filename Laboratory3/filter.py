def predicate(word):
    return word[0]=="h"

words = ["hello", "there", "hello world", "world", "hi"]

print([word for word in words if predicate(word)])
print(list(filter(lambda a : a[0]=='h', words)))
print(list(filter(predicate, words)))