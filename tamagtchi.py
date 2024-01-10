print("------------------------------")
print("Vamos criar seu Tamagochi!")  # --> Mensagem de Boas vindas ao Usuário.
print("------------------------------")

nickname = input("Qual seu nome:")  # --> Guarda o nome do jogador
nome = input("Qual nome do seu Tamagochi:") # --> Guarda o nome do seu Tamagotchi
felicidade = 50  # --> Inicio de sua felicidade
fome = 20  # --> Inicio de sua fome
energia = 40  # --> Inicio de sua energia

print(f"Legal o {nome} está pronto para brincar com você, {nickname}!")  # --> Saudação com o Nome do Jogador e o nome do Tamagotchi

print("------------------------------")

def realizar_acao(escolha): # --> Função que retira e adiciona energia, fome e felicidade
    global felicidade, energia, fome  # --> Declarando as variáveis globais
    if escolha == 1:  # --> Se o usuário escolher um aumenta dez pontos em felicidade e tira dez pontos das outras duas
        felicidade = felicidade + 10    # --> Felicidade ganha dez pontos
        energia = energia - 10  # --> Energia perde dez pontos
        fome = fome - 10    # --> Fome ganha dez pontos
        print(f"Fique esperto em seus medidores:\nEnergia: {energia}%\nFome: {fome}%\nFelicidade: {felicidade}%") # --> Aviso para o usuário ficar esperto e não matar o Tamagotchi
    elif escolha == 2:  # --> Se o usuário escolher dois aumenta dez pontos em energia e tira dez pontos das outras duas
        energia = energia + 10  # --> Energia perde dez pontos
        fome = fome - 10    # --> Fome perde dez pontos
        felicidade = felicidade - 10    # --> Felicidade perde dez pontos
        print(f"Fique esperto em seus medidores:\nEnergia: {energia}%\nFome: {fome}%\nFelicidade: {felicidade}%")   # --> Aviso para o usuário ficar esperto e não matar o Tamagotchi
    elif escolha == 3:  # --> Se o usuário escolher três aumenta dez pontos em felicidade e tira dez pontos das outras duas
        fome = fome + 10 # --> Fome recebe mais dez pontos
        felicidade = felicidade - 10    # --> Felicidade perde dez pontos
        energia = energia - 10  # --> Energia perde dez pontos
        print(f"Fique esperto em seus medidores:\nEnergia: {energia}%\nFome: {fome}%\nFelicidade: {felicidade}%")   # --> Aviso para o usuário ficar esperto e não matar o Tamagotchi
    else:  # --> Se colocar qualquer letra ou número que não seja {1,2.3}
        print("Opção inválida, por favor escolha outra:")  # --> Apresenta mensagem abaixo
    
    morte()

def morte():  # --> Função que chama a morte do personagem
    if felicidade <= 0: # --> Se a felicidade for menor ou igual que zero...
        print(f"AH NÃO, QUE PENA!\n{nome} acaba de morrer de desgosto, sinto muito!")
        exit()  # --> joga o usuário para fora do loop caso a opção acima tenha sido escolhida
    elif felicidade >= 100: # --> Se a felicidade for maior ou igual a cem
        print(f"Você abusou de mais do {nome} acabou matando ele de tanto esforço!")
        exit()  # --> joga o usuário para fora do loop caso a opção acima tenha sido escolhida
    elif fome <= 0: # --> Se a fome for menor ou igual a zero 
        print(f"{nome} estava com tanta fome que acabou morrendo!")
        exit()  # --> joga o usuário para fora do loop caso a opção acima tenha sido escolhida
    elif fome > 100: # --> Se a fome for maior ou igual a cem
        print(f"Você deu muita comida para {nome} e acho que ele comeu algo estragado e morreu!")
        exit()  # --> joga o usuário para fora do loop caso a opção acima tenha sido escolhida
    elif energia <= 0:  # --> Se a energia for menor ou igual a zero
        print(f"Você sobrecarregou muito {nome} e acabou matando ele de cansaço!")
        exit()  # --> joga o usuário para fora do loop caso a opção acima tenha sido escolhida
    elif energia == 100:   # --> Se a energia for igual a cem
        print(f"{nome} está muito bem descansado!\nQuer um conselho de amigo?\nNão o coloque para dormir novamente!")
        exit()  # --> joga o usuário para fora do loop caso a opção acima tenha sido escolhida
    elif energia > 100: # --> Se a energia foi maior que cemm
        print(f"Eu avisei\nAcredite se quiser, {nome} dormiu tanto que acabou morrendo sonhando!")
        exit()  # --> joga o usuário para fora do loop caso a opção acima tenha sido escolhida

rodada = 1   # --> Define que a rodada começa pelo valor númerico um

while True: #--> Estrutura de repetição que cria rodadas e faz a repetição até a morte do Tamagochi
    print(f"\nRodada: {rodada}")  # --> Mostra qual Rodada esta jogando
    escolha = int(input("O que vamos fazer:\n(1) - Brincar\n(2) - Dormir\n(3) - Comer\n(0) - Sair\n"))  # --> A cada rodada recebe o valor que o usuário escolhe
    if escolha == 0:     # --> Se você preferir sair do jogo você abandona seu personagem
        print(f"Você encerrou o jogo. {nome} morreu de solidão!")    # --> Mensagem de encerramento
        break
    realizar_acao(escolha)  # --> Função que recebe valor escolha
    rodada += 1 