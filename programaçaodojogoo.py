print("sanidade quebrada")
print("bem vindo ao jogo")
print("o jogo se passa em um teatro abandonado onde os pessonagens foram explorar ate que eles se deparam com um marionete que se move e ela o atacalos")

print("personagem 1: lucas")
print("personagem 2: helena")
print("inimigo marionet quebrada")
import random

print(" escolha seu personagem: 1 para lucas, 2 para helena para essa batalha contra a marionete quebrada")
personagem = int(input())  
if personagem == 1:    print("lucas")
elif personagem == 2:    print("helena")
else:    print("personagem invalido")

if personagem == 1:
    print(" escolha seu ataque: 1 para golpe direto, 2 para pulso de luz, 3 para colapso controlado")
    ataque = int(input())
    if ataque == 1:    print("lucas usou golpe direto e causou 25 de dano")
    elif ataque == 2:    print("lucas usou pulso de luz e causou 35 de dano")
    elif ataque == 3:    print("lucas usou colapso controlado e causou 50 de dano")
else:    print("ataque invalido")

if personagem == 2:
    print(" escolha seu ataque: 1 para golpe com objeto, 2 para movimento rapido, 3 para pressao psicologica")
    ataque = int(input())
    if ataque == 1:    print("helena usou golpe com objeto e causou 25 de dano")
    elif ataque == 2:    print("helena usou movimento rapido e causou 30 de dano")
    elif ataque == 3:    print("helena usou pressao psicologica e causou 40 de dano")
else:    print("ataque invalido")

print("vez da marionete quebrada ")

ataque_inimigo = random.randint(1,3)
if ataque_inimigo == 1:    print("a marionete quebrada usou imitar e causou 20 de dano")
elif ataque_inimigo == 2:    print("a marionete quebrada usou fios invisiveis e causou 15 de dano")
elif ataque_inimigo == 3:    print("a marionete quebrada usou controle forçado e causou 30 de dano")

print (" vida final dos personagens")
if personagem == 1 and ataque == 1:   print("lucas tem 80 de vida restante")
elif personagem == 1 and ataque == 2:  print("lucas tem 70 de vida restante")
elif personagem == 1 and ataque == 3:  print("lucas tem 50 de vida restante")
elif personagem == 2 and ataque == 1:    print("helena tem 65 de vida restante")
elif personagem == 2 and ataque == 2:   print("helena tem 60 de vida restante")
elif personagem == 2 and ataque == 3: print("helena tem 50 de vida restante")

if personagem == 1 and ataque == 1:   print("a marionete quebrada tem 55 de vida restante")
elif personagem == 1 and ataque == 2: print("a marionete quebrada tem 45 de vida restante")
elif personagem == 1 and ataque == 3:   print("a marionete quebrada tem 30 de vida restante")
elif personagem == 2 and ataque == 1:    print("a marionete quebrada tem 60 de vida restante")
elif personagem == 2 and ataque == 2:  print("a marionete quebrada tem 50 de vida restante")
elif personagem == 2 and ataque == 3:   print("a marionete quebrada tem 40 de vida restante")