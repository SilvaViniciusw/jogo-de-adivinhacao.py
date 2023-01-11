 print("*********************************")
    print("bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 100

    print("qual nivel de dificuldade ?")
    print("(1) Fácil (2) médio (3) difícil")

    nivel = int(input("define o nivel:"))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas+1):
        print("tentativa {} de {}". format(rodada, total_de_tentativas))

        chute_str = input("digite um número entre 1 e 100 :")
        chute = int(chute_str)
        print("voce digitou o numero", chute)


        if(chute < 1 or chute > 100):
            print("vocÊ deve digitar um numero entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("você errou ! o seu numero foi maior que o numero secreto.")
                if (rodada == total_de_tentativas):
                    print("você errou, o numero secreto era {} e você fez {} pontos!".format(numero_secreto,pontos))
            elif (menor):
                print("você errou! o seu numero foi menor que o numero secreto.")
            pontos_perdidos = round(abs(numero_secreto - chute))
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")
