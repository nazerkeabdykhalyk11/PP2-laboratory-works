def is_palindrome(word):
    reversed_word = ""
    for i in range(1,len(word)+1):
        reversed_word += word[-i]

    if word == reversed_word:
        return True
    else:
        return False
    

print(is_palindrome(str(input(f'Enter any word: '))))