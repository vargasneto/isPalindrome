def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


text = input("Digite duas ou mais palavras: ")
words = text.split()
palindromes = []

for word in words:
    if is_palindrome(word):
        palindromes.append(word)

if not words:
    print("Nenhuma palavra informada")
elif palindromes:
    print("Palindromos encontrados:")
    for word in palindromes:
        print(word)
else:
    print("Nenhuma palavra e palindromo")
