print("///////////////////////////////////////////")
print("////////////sanidade quebrada//////////////")
print("///////////////////////////////////////////")
print("////////////bem vindo ao jogo//////////////")
print("///////////////////////////////////////////")
print("o jogo se passa em um teatro abandonado onde os personagens foram explorar ate que eles se deparam com uma marionete que se move e ela os ataca")
print("///////////////////////////////////////////")
print("personagem 1: lucas")
print("personagem 2: helena")
print("inimigo: marionete quebrada")

import random
import time

print("escolha seu personagem: 1 para lucas, 2 para helena")
personagem = int(input())
dados_batalha = {
"vida_lucas": 100,
"vida_helena": 90,
"vida_inimigo": 110,

"ataque":[
 ("efeito_pulso", 0)
 ("efeito_pressao",0)
]
}

if personagem == 1:
    print("voce escolheu lucas")
    vida_jogador = {dados_batalha("vida_lucas")}

elif personagem == 2:
    print("voce escolheu helena")
    vida_jogador ={dados_batalha("vida_helena")}

else:
    print("personagem invalido")
    exit()

print("///////////////////////////////////////////")

for i in range(1, 6):

    print(f"\nessa e sua {i} rodada")
    print(f"vida do jogador: {vida_jogador}")
    print(f"vida da marionete quebrada: {vida_inimigo}")

    if efeito_pulso > 0:
        vida_inimigo -= 10
        efeito_pulso -= 1
        print("o pulso de luz causou mais 10 de dano continuo!")

    if efeito_pressao > 0:

        for i in range(4):
            vida_inimigo -= 10
            print("a pressao psicologica causou 10 de dano mental!")
            time.sleep(0.5)

        efeito_pressao = 0

    if vida_inimigo <= 0:
        print("a marionete quebrada foi derrotada!")
        break

    if personagem == 1:

        print("escolha seu ataque:")
        print("1 para golpe direto")
        print("2 para pulso de luz")
        print("3 para colapso controlado")

        ataque = int(input())

        if ataque == 1:
            dano = 25
            print("lucas usou golpe direto e causou 25 de dano")

        elif ataque == 2:
            dano = 20
            efeito_pulso = 3
            print("lucas usou pulso de luz e causou 20 de dano")

        elif ataque == 3:
            dano = 50
            print("lucas usou colapso controlado e causou 50 de dano")

        else:
            dano = 0
            print("ataque invalido")

    elif personagem == 2:

        print("escolha seu ataque:")
        print("1 para golpe com objeto")
        print("2 para movimento rapido")
        print("3 para pressao psicologica")

        ataque = int(input())

        if ataque == 1:
            dano = 25
            print("helena usou golpe com objeto e causou 25 de dano")

        elif ataque == 2:
            dano = 30
            print("helena usou movimento rapido e causou 30 de dano")

        elif ataque == 3:
            dano = 0
            efeito_pressao = 1
            print("helena usou pressao psicologica!")
            print("a mente da marionete esta entrando em colapso!")

        else:
            dano = 0
            print("ataque invalido")

    vida_inimigo -= dano

    if vida_inimigo <= 0:
        print("a marionete quebrada foi derrotada!")
        break

    time.sleep(2)

    print("\nvez da marionete quebrada")

    ataque_inimigo = random.randint(1, 3)

    if ataque_inimigo == 1:
        dano_inimigo = 20
        print("a marionete quebrada usou imitar e causou 20 de dano")

    elif ataque_inimigo == 2:
        dano_inimigo = 15
        print("a marionete quebrada usou fios invisiveis e causou 15 de dano")

    elif ataque_inimigo == 3:
        dano_inimigo = 30
        print("a marionete quebrada usou controle forcado e causou 30 de dano")

    vida_jogador -= dano_inimigo

    if vida_jogador <= 0:
        print("voce foi derrotado pela marionete quebrada...")
        break

print("\n///////////////////////////////////////////")
print(f"vida final do jogador: {vida_jogador}")
print(f"vida final da marionete quebrada: {vida_inimigo}")
print("fim da batalha")