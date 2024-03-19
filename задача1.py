n = int(input("Введите количество слов: "))
resultat = ""
for i in range(n):
    word = input("Введите слово: ")
    resultat += word + " "
print("Результат:", resultat)