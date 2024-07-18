import random
import time

player = 0
num = random.randint(1,10)
while player != num:
    player = int(input("Digite um Número de 1 a 10: "))
    if player > num:
        print("Tente um número menor")
        time.sleep(1)
    elif player < num:
        print("Tente um número maior")
        time.sleep(1)
    else:
        print("Você acertou, o número era",num)