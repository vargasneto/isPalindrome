def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


text = input("Digite uma palavra: ")

if is_palindrome(text):
    print("Is Palindrome!")
else:
    print("Not is palindrome")
