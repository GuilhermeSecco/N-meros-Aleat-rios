import random
import time

num = 0
min = 1
max = 100
resposta = ""

print("Escolha um número entre 1 e 100, o computador vai tentar adivinhar")
time.sleep(2)

while resposta != "C":
    num = random.randint(min,max)
    print('O número escolhido é (M)aior ou me(N)or que', num, ',caso o número esteja correto utilize C')
    resposta = input()
    resposta = resposta.upper()
    if resposta == "M":
        min = num + 1
    elif resposta == "N":
        max = num - 1
    elif resposta == "C":
        print("O valor escolhido foi", num)
    else:
        print("Por favor, escolha uma resposta válida")