print("------------------------------")
print("Vamos criar seu Tamagochi!")  # --> Mensagem de Boas vindas ao Usuário.
print("------------------------------")

nickname = input("Qual seu nome:")  # --> Guarda o nome do jogador
nome = input("Qual nome do seu Tamagochi:") # --> Guarda o nome do seu Tamagotchi
felicidade = 50  # --> Inicio de sua felicidade
fome = 20  # --> Inicio de sua fome
energia = 40  # --> Inicio de sua energia

print(f"Legal o {nome} está pronto para brincar com você, {nickname}!")

print("------------------------------")

def realizar_acao(escolha): # --> Função que retira e adiciona energia, fome e felicidade
    global felicidade, energia, fome  # --> Declarando as variáveis globais
    if escolha == 1:
        felicidade = felicidade + 10
        energia = energia - 10
        fome = fome - 10
        print(f"Fique esperto em seus medidores:\nEnergia: {energia}%\nFome: {fome}%\nFelicidade: {felicidade}%")
    elif escolha == 2:
        energia = energia + 10
        fome = fome - 10
        felicidade = felicidade - 10
        print(f"Fique esperto em seus medidores:\nEnergia: {energia}%\nFome: {fome}%\nFelicidade: {felicidade}%")
    elif escolha == 3:
        fome = fome + 10
        felicidade = felicidade - 10
        energia = energia - 10
        print(f"Fique esperto em seus medidores:\nEnergia: {energia}%\nFome: {fome}%\nFelicidade: {felicidade}%")
    else:
        print("Opção inválida, por favor escolha outra:")
    
    morte()

def morte():  # --> Função que chama a morte do personagem
    if felicidade <= 0:
        print(f"AH NÃO, QUE PENA!\n{nome} acaba de morrer de desgosto, sinto muito!")
        exit()
    elif felicidade >= 100:
        print(f"Você abusou de mais do {nome} acabou matando ele de tanto esforço!")
        exit()
    elif fome <= 0:
        print(f"{nome} estava com tanta fome que acabou morrendo!")
        exit()
    elif fome > 100:
        print(f"Você deu muita comida para {nome} e acho que ele comeu algo estragado e morreu!")
        exit()
    elif energia <= 0:
        print(f"Você sobrecarregou muito {nome} e acabou matando ele de cansaço!")
        exit()
    elif energia == 100:
        print(f"{nome} está muito bem descansado!\nQuer um conselho de amigo?\nNão o coloque para dormir novamente!")
        exit()
    elif energia > 100:
        print(f"Eu avisei\nAcredite se quiser, {nome} dormiu tanto que acabou morrendo sonhando!")
        exit()

rodada = 1  

while True: #--> Estrutura de repetição que cria rodadas e faz a repetição até a morte do Tamagochi
    print(f"\nRodada {rodada}")
    escolha = int(input("O que vamos fazer:\n(1) - Brincar\n(2) - Dormir\n(3) - Comer\n(0) - Sair\n"))
    if escolha == 0:
        print(f"Você encerrou o jogo. {nome} morreu de solidão!")
        break
    realizar_acao(escolha)
    rodada += 1