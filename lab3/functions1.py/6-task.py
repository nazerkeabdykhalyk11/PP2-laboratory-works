def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

user_input = input("Enter a sentence: ")
result = reverse_sentence(user_input)
print(result)
