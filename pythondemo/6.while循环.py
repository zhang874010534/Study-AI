word_length = 0
while word_length < 5:
    print(word_length)
    word_length += 1

lst = [1, 2, 3, 4]
for i in range(len(lst)):
    if lst[i] == 3:
        continue
        # break
    print(lst[i])