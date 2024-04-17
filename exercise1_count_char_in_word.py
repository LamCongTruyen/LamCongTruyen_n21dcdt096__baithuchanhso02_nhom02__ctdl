def count_chars_in_word(word):
    char_count = {}

    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

# Ví dụ:
word = "CAU TRUC DU LIEU"
char_count = count_chars_in_word(word)
print("Dictionary đếm số chữ trong một từ:", char_count)
