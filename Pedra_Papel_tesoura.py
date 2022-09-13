from random import choice

jogador_vitorias = 0
maquinas_vitorias = 0

def opcao_do_jogador():
    esc_jogador = input("Escolha Pedra,Papel ou Tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        print("Opcao Invalida. Tente novamente")
        opcao_do_jogador()


def opcao_da_maquina():
    escolha_da_maquina = choice(["pedra","papel","tesoura"])
    return escolha_da_maquina



while True:
    print("-"*30)

    esc_jogador = opcao_do_jogador()
    op_da_maquina = opcao_da_maquina()

    print("-"*30)

    if(esc_jogador == "pedra") and (op_da_maquina == "tesoura") \
        or (esc_jogador == "papel") and (op_da_maquina == "pedra")\
            or (esc_jogador == "tesoura") and (op_da_maquina == "papel"):

            print(f"Jogador escolheu{esc_jogador} e a Maquina escolheu {op_da_maquina} Resultado:"
            " Resultado : Voce Ganhou!")
            jogador_vitorias += 1
        
    elif esc_jogador == op_da_maquina:
        print(f"Jogador escolheu{esc_jogador} e a Maquina escolheu {op_da_maquina} Resultado:"
            " Resultado : Empate!")
    else:
        print(f"Jogador escolheu{esc_jogador} e a Maquina escolheu {op_da_maquina} Resultado:"
            " Resultado : Voce Perderu!")
        maquinas_vitorias += 1




    print("-"*30)
    print(f"Virtorias do Jogador: {jogador_vitorias}")
    print(f"Virtorias da Maquina: {maquinas_vitorias}")
    print("-"*30)

    esc_jogador = input("Voce quer jogar novamente: ")
    if esc_jogador in ["Sim","sim","s","S","SIM"]:
        pass
    elif esc_jogador in ["NAO","Nao","n","nao"]:
        print("Obrigado Por jogar :)")
        break
    else:
        break