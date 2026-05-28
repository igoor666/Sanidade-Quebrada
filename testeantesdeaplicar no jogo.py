
import random
import time

print("///////////////////////////////////////////")
print("////////////sanidade quebrada//////////////")
print("///////////////////////////////////////////")
print("////////////bem vindo ao jogo//////////////")
print("///////////////////////////////////////////\n")

jogador = {
    "nome": "Lucas",
    "vida_atual": 100,
    "vida_maxima": 100,
    "pocoes_disponiveis": {"Poção Pequena": 2},
    "ataques": ["Golpe Direto", "Pulso de Luz", "Colapso Controlado"]
}

inimigo = {
    "nome": "Marionete Quebrada",
    "vida_atual": 120,
    "vida_maxima": 120,
    "pocoes_disponiveis": {"Poção Pequena": 1},
    "ataques": ["Imitar", "Fios Invisíveis", "Controle Forçado"]
}

ataques = {
    "Golpe Direto": {"dano_base": 25, "tipo": "normal"},
    "Pulso de Luz": {"dano_base": 12, "tipo": "persistente", "persistencia": {"dano": 8, "turnos": 3}},
    "Colapso Controlado": {"dano_base": 10, "tipo": "multidano", "golpes": 4},
    "Imitar": {"dano_base": 20, "tipo": "normal"},
    "Fios Invisíveis": {"dano_base": 15, "tipo": "normal"},
    "Controle Forçado": {"dano_base": 30, "tipo": "normal"}
}

pocoes = {
    "Poção Pequena": 30
}

efeito_persistente = {"alvo": None, "dano": 0, "turnos": 0}

print("Status inicial:")
print(f"{jogador['nome']}: {jogador['vida_atual']} de vida")
print(f"{inimigo['nome']}: {inimigo['vida_atual']} de vida\n")

primeiro = random.choice(["jogador", "inimigo"])
if primeiro == "jogador":
    print("O jogador atacará primeiro.\n")
else:
    print("A marionete quebrada atacará primeiro.\n")

turno = primeiro

while jogador["vida_atual"] > 0 and inimigo["vida_atual"] > 0:
    if efeito_persistente["turnos"] > 0:
        if efeito_persistente["alvo"] == "inimigo":
            inimigo["vida_atual"] -= efeito_persistente["dano"]
            print(f"Efeito persistente: {inimigo['nome']} sofre {efeito_persistente['dano']} de dano.")
        efeito_persistente["turnos"] -= 1
        if efeito_persistente["turnos"] == 0:
            efeito_persistente["alvo"] = None

    if inimigo["vida_atual"] <= 0:
        break

    print("===========================================")
    print(f"Vida {jogador['nome']}: {jogador['vida_atual']} / {jogador['vida_maxima']}")
    print(f"Vida {inimigo['nome']}: {inimigo['vida_atual']} / {inimigo['vida_maxima']}")
    print("===========================================\n")

    if turno == "jogador":
        print("Seu turno:")
        print("[1] Atacar")
        print("[2] Usar Poção")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "2":
            if sum(jogador["pocoes_disponiveis"].values()) == 0:
                print("Você não tem poções disponíveis.\n")
            else:
                print("\nPoções disponíveis:")
                for i, (nome, qtd) in enumerate(jogador["pocoes_disponiveis"].items(), start=1):
                    print(f"{i} - {nome} ({qtd})")
                opcao = input("Escolha a poção: ").strip()
                if opcao.isdigit():
                    opcao = int(opcao) - 1
                    if 0 <= opcao < len(jogador["pocoes_disponiveis"]):
                        nome_pocao = list(jogador["pocoes_disponiveis"].keys())[opcao]
                        if jogador["pocoes_disponiveis"][nome_pocao] > 0:
                            jogador["pocoes_disponiveis"][nome_pocao] -= 1
                            cura = pocoes[nome_pocao]
                            vida_antes = jogador["vida_atual"]
                            jogador["vida_atual"] = min(jogador["vida_atual"] + cura, jogador["vida_maxima"])
                            print(f"Você usou {nome_pocao} e recuperou {jogador['vida_atual'] - vida_antes} de vida.\n")
                        else:
                            print("Poção sem quantidade.\n")
                turno = "inimigo"
                continue

        print("\nAtaques:")
        for i, nome_ataque in enumerate(jogador["ataques"], start=1):
            print(f"{i} - {nome_ataque}")
        escolha_ataque = input("Escolha o ataque: ").strip()

        if not (escolha_ataque.isdigit() and 1 <= int(escolha_ataque) <= len(jogador["ataques"])):
            print("Ataque inválido.\n")
            turno = "inimigo"
            continue

        ataque_nome = jogador["ataques"][int(escolha_ataque) - 1]
        ataque = ataques[ataque_nome]

        dano = 0
        if ataque["tipo"] == "normal":
            dano = random.randint(max(1, ataque["dano_base"] - 4), ataque["dano_base"] + 4)
        elif ataque["tipo"] == "multidano":
            golpes = ataque["golpes"]
            for _ in range(golpes):
                dano += random.randint(max(1, ataque["dano_base"] - 3), ataque["dano_base"] + 3)
            print(f"{ataque_nome} acertou {golpes} vezes.")
        elif ataque["tipo"] == "persistente":
            dano = random.randint(max(1, ataque["dano_base"] - 3), ataque["dano_base"] + 3)
            efeito_persistente = {
                "alvo": "inimigo",
                "dano": ataque["persistencia"]["dano"],
                "turnos": ataque["persistencia"]["turnos"]
            }

        inimigo["vida_atual"] -= dano
        print(f"{jogador['nome']} usou {ataque_nome} e causou {dano} de dano.\n")
        turno = "inimigo"

    else:
        print("Turno do inimigo:")
        curar = (
            inimigo["vida_atual"] <= inimigo["vida_maxima"] * 0.30
            and inimigo["pocoes_disponiveis"].get("Poção Pequena", 0) > 0
            and random.randint(1, 100) <= 10
        )
        if curar:
            inimigo["pocoes_disponiveis"]["Poção Pequena"] -= 1
            cura = pocoes["Poção Pequena"]
            vida_antes = inimigo["vida_atual"]
            inimigo["vida_atual"] = min(inimigo["vida_atual"] + cura, inimigo["vida_maxima"])
            print(f"{inimigo['nome']} usou Poção Pequena e recuperou {inimigo['vida_atual'] - vida_antes} de vida.\n")
            turno = "jogador"
            continue

        ataque_nome = random.choice(inimigo["ataques"])
        ataque = ataques[ataque_nome]
        dano = random.randint(max(1, ataque["dano_base"] - 4), ataque["dano_base"] + 4)
        jogador["vida_atual"] -= dano
        print(f"{inimigo['nome']} usou {ataque_nome} e causou {dano} de dano.\n")
        turno = "jogador"

    time.sleep(1)

if inimigo["vida_atual"] <= 0:
    print(f"{inimigo['nome']} foi derrotado. {jogador['nome']} venceu!")
elif jogador["vida_atual"] <= 0:
    print(f"{jogador['nome']} foi derrotado. {inimigo['nome']} venceu!")
else:
    print("A batalha terminou.")

print("\nStatus final:")
print(f"{jogador['nome']}: {jogador['vida_atual']} de vida")
print(f"{inimigo['nome']}: {inimigo['vida_atual']} de vida")