import random
import time

print("///////////////////////////////////////////")
print("////////////sanidade quebrada//////////////")
print("///////////////////////////////////////////")
print("////////////bem vindo ao jogo//////////////")
print("///////////////////////////////////////////")

personagens = {

    1: {
        "nome": "lucas",
        "vida": 100,

        "ataques": [

            {
                "nome": "golpe direto",
                "dano": 25
            },

            {
                "nome": "pulso de luz",
                "dano": 20,
                "efeito": "pulso"
            },

            {
                "nome": "colapso controlado",
                "dano": 50,
                "sanidade_max": 40
            }
        ]
    },

    2: {
        "nome": "helena",
        "vida": 90,

        "ataques": [

            {
                "nome": "golpe com objeto",
                "dano": 25
            },

            {
                "nome": "movimento rapido",
                "dano": 30
            },

            {
                "nome": "pressao psicologica",
                "dano": 0,
                "efeito": "pressao",
                "sanidade_max": 40
            }
        ]
    }
}

inimigo = {
    "nome": "marionete quebrada",
    "vida": 120
}

ataques_inimigo = [

    {
        "nome": "imitar",
        "dano": 20,
        "sanidade": 15
    },

    {
        "nome": "fios invisiveis",
        "dano": 15,
        "sanidade": 15
    },

    {
        "nome": "controle forcado",
        "dano": 30,
        "sanidade": 25
    }
]

itens = [

    {
        "nome": "kit medico",
        "quantidade": 2,
        "cura": 35
    },

    {
        "nome": "calmante",
        "quantidade": 2,
        "sanidade": 30
    },

    {
        "nome": "amuleto",
        "quantidade": 1,
        "defesa": 10
    }
]

print("personagem 1: lucas")
print("personagem 2: helena")

print("\nescolha seu personagem")
personagem = int(input())

if personagem not in personagens:
    print("personagem invalido")
    exit()

jogador = personagens[personagem]

vida_jogador = jogador["vida"]
vida_inimigo = inimigo["vida"]

sanidade = 100

efeito_pulso = 0
efeito_pressao = 0
defesa = 0

print(f"\nvoce escolheu {jogador['nome']}")

for rodada in range(1, 6):

    print("\n///////////////////////////////////////////")
    print(f"rodada {rodada}")
    print(f"vida do jogador: {vida_jogador}")
    print(f"sanidade: {sanidade}")
    print(f"vida da marionete: {vida_inimigo}")

    if efeito_pulso > 0:
        vida_inimigo -= 10
        efeito_pulso -= 1

        print("pulso de luz causou 10 de dano continuo")

    if efeito_pressao > 0:

        for i in range(4):

            vida_inimigo -= 10

            print("pressao psicologica causou 10 de dano mental")

            time.sleep(0.5)

        efeito_pressao = 0

    if vida_inimigo <= 0:
        print("a marionete quebrada foi derrotada")
        break

    print("\n1 = atacar")
    print("2 = usar item")

    escolha = int(input())

    dano = 0

    if escolha == 2:

        print("\nitens:")

        for i in range(len(itens)):

            print(f"{i+1} = {itens[i]['nome']} ({itens[i]['quantidade']})")

        item = int(input())

        if item >= 1 and item <= len(itens):

            item_escolhido = itens[item - 1]

            if item_escolhido["quantidade"] > 0:

                item_escolhido["quantidade"] -= 1

                if item_escolhido["nome"] == "kit medico":

                    vida_jogador += item_escolhido["cura"]

                    print("vida recuperada")

                elif item_escolhido["nome"] == "calmante":

                    sanidade += item_escolhido["sanidade"]

                    if sanidade > 100:
                        sanidade = 100

                    print("sanidade recuperada")

                elif item_escolhido["nome"] == "amuleto":

                    defesa = item_escolhido["defesa"]

                    print("o dano recebido sera reduzido")

            else:
                print("item sem quantidade")

    else:

        print("\nataques:")

        for i in range(len(jogador["ataques"])):

            print(f"{i+1} = {jogador['ataques'][i]['nome']}")

        escolha_ataque = int(input())

        if escolha_ataque >= 1 and escolha_ataque <= len(jogador["ataques"]):

            ataque = jogador["ataques"][escolha_ataque - 1]

            if "sanidade_max" in ataque:

                if sanidade > ataque["sanidade_max"]:

                    print("sanidade muito alta para usar esse ataque")

                    dano = 0

                else:

                    dano = ataque["dano"]

                    print(f"{jogador['nome']} usou {ataque['nome']}")

            else:

                dano = ataque["dano"]

                print(f"{jogador['nome']} usou {ataque['nome']}")

            if "efeito" in ataque:

                if ataque["efeito"] == "pulso":

                    efeito_pulso = 3

                    print("o inimigo sofrera dano continuo")

                elif ataque["efeito"] == "pressao":

                    efeito_pressao = 1

                    print("a mente da marionete esta entrando em colapso")

    vida_inimigo -= dano

    if vida_inimigo <= 0:

        print("a marionete quebrada foi derrotada")

        break

    time.sleep(1)

    print("\nvez da marionete quebrada")

    ataque_inimigo = random.choice(ataques_inimigo)

    dano_inimigo = ataque_inimigo["dano"]

    perda_sanidade = ataque_inimigo["sanidade"]

    if defesa > 0:

        dano_inimigo -= defesa

        if dano_inimigo < 0:
            dano_inimigo = 0

        print("o amuleto reduziu o dano")

    print(f"a marionete usou {ataque_inimigo['nome']}")

    print(f"causou {dano_inimigo} de dano")

    vida_jogador -= dano_inimigo

    sanidade -= perda_sanidade

    if sanidade < 0:
        sanidade = 0

    print(f"sua sanidade caiu {perda_sanidade}")


    if sanidade <= 20:

        print("sua mente esta entrando em colapso...")

    if vida_jogador <= 0:

        print("voce foi derrotado")

        break

    if sanidade <= 0:

        print("voce enlouqueceu")

        break

print("\n///////////////////////////////////////////")
print("fim da batalha")
print(f"vida final: {vida_jogador}")
print(f"sanidade final: {sanidade}")
print(f"vida da marionete: {vida_inimigo}")           