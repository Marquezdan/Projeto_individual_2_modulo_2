#----------------------------------------------------
# Formação Analise de dados Resilia|Senac
# Autor: Daniel Marques
# Projeto Individual 2 do Módulo 2 : "Contratado!"
#----------------------------------------------------
#####python programação desenvolvimento
candidatosVaga1 = {}
candidatosVaga2 = {}
candidatosApv1 =  {}
candidatosApv2 =  {}
# Dicionários que vão recebeber todos os candidatos inscritos para as vagas 1 e vaga 2, e os aprovados para as mesmas.

def aptoVaga(): # Função que recebe o nome, resumo\miniBio do candidato e para qual vaga ele deseja se candidatar. 
    sair = 1
    while sair != 0: # Estrutura de repetição para o cadastro de vários usuários.
        nome = input("Digite o seu primeiro nome: \n")
        resumo = input("Faça um breve resumo sobre o seu currículo: \n")
        try: 
            selecionarVaga = int(input("Selecione para qual vaga você deseja se cadastrar digitando 1 ou 2, onde, 1 = Desevolvedor java e 2 = Analista de dados:\n"))
        except: 
            print("\n Opcão inválida, digite o nome e o resumo novamente e escolha uma das vagas válidas.")
            continue

        if selecionarVaga == 1: candidatosVaga1.update({nome:resumo}) 
        elif selecionarVaga == 2: candidatosVaga2.update({nome:resumo})
        else: 
            pass
        
        if "python" and "programação" and "desenvolvimento" in resumo: # Condicional que checa se as palavras chaves indicadas para a vaga 1 estão no resumo\minibio
            candidatosApv1.update({nome:resumo})
        if  "Análise de dados" and "dados" and "SQL" in resumo: # Condicional que checa se as palavras chaves indicadas para a vaga 1 estão no resumo\minibio
            candidatosApv2.update({nome:resumo})
        sair = int(input("Deseja continuar cadastrando usuários? Digite 1 para sim e 0 para não:\n"))   

    #imprime o número de candidatos que se inscreveu para cada vaga e quais estão aptos.
    print(f" O número de candidatos totais para vaga 1 é de {len(candidatosVaga1)} pessoas.")
    print(f" O número de candidatos totais para vaga 2 é de {len(candidatosVaga2)} pessoas.")
    print(f" O número de candidatos aptos a vaga 1 é de {len(candidatosApv1)} pessoas.")
    print(f" O número de candidatos aptos a vaga 1 é de {len(candidatosApv2)} pessoas.")


aptoVaga() #Chama a função.
