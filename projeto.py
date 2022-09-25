import json

#importar arquivos sobre as questões
with open("questoes.json") as file:
    questoes = json.load(file)
with open("opcoes.json") as file:
    opcoes = json.load(file)
with open("dificuldades.json") as file:
    dificuldade = json.load(file)

podio = {}
pontuacao = 0

#questões-opções-respostas
def novo_jogo():

    lista_Respostas = []
    respostas_corretas = 0
    questao_num = 1
    dificuldade_num = 0
    pontuacao = 0
    for x in questoes:
        print("-------------------------")
        print(x)
        for i in opcoes[questao_num-1]:
            print(i)
        dificuldade_questao = dificuldade[dificuldade_num]
        print(f"Nível de dificuldade: {dificuldade_questao.upper()}")
        resposta = input("Digite (A, B, C, ou D): ")
        resposta = resposta.upper()
        lista_Respostas.append(resposta)

        respostas_corretas += Confirmar_Respostas(questoes.get(x), resposta, dificuldade_questao)
        questao_num += 1
        dificuldade_num += 1

    mostrar_pontuação(respostas_corretas, lista_Respostas)

# -------------------------comparar a resposta do usuário com a resposta cadastrada.
def Confirmar_Respostas(resposta_usuario, resposta, dificuldade_questao):
    if resposta_usuario == resposta:
        print("CORRETO!")
        calcular_pontuacao(dificuldade_questao)
        return 1
    else:
        print("ERRADO!")
        return 0

def calcular_pontuacao(dificuldade_questao):
    global pontuacao
    if dificuldade_questao.upper() == "FÁCIL":
        print("Você ganhou 10 pontos!")
        pontuacao += 10
    elif dificuldade_questao.upper() == "MÉDIO":
        print("Você ganhou 20 pontos!")
        pontuacao += 15
    elif dificuldade_questao.upper() == "DIFÍCIL":
        print("Você ganhou 30 pontos!")
        pontuacao += 25
# ------------------------- mostra as respostas corretas-respostas que o usuário digitou-pountuação
def mostrar_pontuação(respostas_corretas, lista_Respostas):
    global pontuacao
    print("-------------------------")
    print("RESULTADOS")
    print("-------------------------")

    print("RESPOSTAS CORRETAS: ", end="")
    for i in questoes:
        print(questoes.get(i), end=" ")
    print()

    print("RESPOSTAS DO USUÁRIO: ", end="")
    for i in lista_Respostas:
        print(i, end=" ")
    print()

    NomeJogador = str(input("Digite o nome do Jogador! "))
    print("Sua pontuação é: "+str(pontuacao)+"")
    podio.update({f'{NomeJogador}': pontuacao})
    pontuacao = 0

# -------------------------
def Nova_Rodada(): #se  o jogador disser sim, uma nova rodada irá se iniciar

    jogarnovamente = input("Deseja jogar novamente? (sim ou não): ")
    jogarnovamente = jogarnovamente.upper()

    if jogarnovamente == "SIM":
        return True
    else:
        return False
# -------------------------

#INICIO

while True:
    resposta = int(input(f"Seja bem vindo ao Jogo de Perguntas! Digite 1, para iniciar.\n 1 - Iniciar Quiz: "))
    if resposta == 1:
        novo_jogo()

        while Nova_Rodada():
            novo_jogo()

        print("Fim de jogo!")

        #Imprimir pontuação decrescente, caso tenha mais de um jogador na rodada.
        if len(podio) > 1:
            print("-=" * 20)
            print ("Pódio")
            print("-=" * 20)
            for i in sorted(podio, key = podio.get, reverse=True):
                print(f"{i} ----- {podio[i]}pts")
            with open(f'RANKING.txt', 'w') as f:
                            f.write(f"RANKING \n")
                            for i in sorted(podio, key = podio.get, reverse=True):
                                    f.write(f"{i} ----- {podio[i]}pts\n")
                            print("O arquivo RANKING.txt foi gerado e salvo no diretório do programa.")
        print("Obrigado por utilizar o programa!")
        break