#   python programação desenvolvimento

candidatosVaga1 ={}
candidatosVaga2 ={}
candidatosApv1 = {}
candidatosApv2 = {}


def aptoVaga():
    sair = 1
    while sair != 0:
        nome = input("Digite o seu primeiro nome: \n").title
        resumo = input("Faça um breve resumo sobre o seu currículo: \n").title
        try: 
            selecionarVaga = int(input("Selecione para qual vaga você deseja se cadastrar digitando 1 ou 2, onde, 1 = Desevolvedor java e 2 = Analista de dados:\n"))
        except: 
            print("\n Opcão inválida, digite o nome e o resumo novamente e escolha uma das vagas válidas.")
            continue

        if selecionarVaga == 1: candidatosVaga1.update({nome:resumo}) 
        elif selecionarVaga == 2: candidatosVaga2.update({nome:resumo})
        else: pass
        if "Python" and "Programação" and "Desenvolvimento" in resumo:candidatosApv1.update({nome:resumo})
        if  "Análise de dados" and "Dados" and "SQL" in resumo:candidatosApv2.update({nome:resumo})
        sair = int(input("Deseja continuar cadastrando usuários? Digite 1 para sim e 0 para não:\n"))   

    print(f" O número de candidatos totais para vaga 1 é de{len(candidatosVaga1)} pessoas.")
    print(f" O número de candidatos totais para vaga 2 é de{len(candidatosVaga2)} pessoas.")
    print(f" O número de candidatos aptos a vaga 1 é de {len(candidatosApv1)} pessoas.")
    print(f" O número de candidatos aptos a vaga 1 é de {len(candidatosApv2)} pessoas.")


aptoVaga()
