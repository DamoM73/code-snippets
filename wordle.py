word_1 = "hello"
word_2 = "jello"
word_3 = ""

index = 0

while index < len(word_1):
    print(word_1[index], word_2[index])
    word_3 = word_3 + "#"
    index = index + 1
    
print(word_3)