# 👾 Tamagotchi

## 🟢 Status: Finalizado 📅 Publicado: 10/01/2024 🧍‍♂️ Programador: muuhlirø
#### Este foi o meu emocionante ponto de partida, meu primeiro passo no mundo da programação. Foi a primeira vez que minhas palavras ganharam vida em forma de código. Espero que vocês tenham sentido a empolgação que eu senti ao criar isso. A inspiração veio de um desejo profundo de reviver um jogo que eu costumava jogar quando tinha apenas 5 anos. Este projeto é uma jornada nostálgica que me conecta com as lembranças carinhosas de meus avós e pais, que, com sorrisos nos rostos, compraram esse mini game na feira para mim. A cada linha de código, revive-se uma parte do meu passado, e compartilho esse sentimento com vocês.
## Como funciona?

#### Um Tamagotchi é um amigo Virtual que você precisa cuidar dele alimentando, fazendo o descançar e brincando com ele mas deve tomar cuidado para não mata-lo alimenta-lo na hora certa e não abusar de mais das opções pois tudo que é exagerado pode vim a fazer mal.

## 👨‍💻 Veja como o jogo foi códificado abaixo: 
#### Fique a vontade para copiar e rodar na sua maquina ou em algum emulador de código python que eu irei deixar no final do Redme.
```python
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
```

## 🎮 PlayGame!

#### Quando você começa o jogo a primeira coisa que ele te pede é seu nome:
![](https://media.discordapp.net/attachments/1194334339954131054/1194712817597690006/image.png?ex=65b15a04&is=659ee504&hm=d07d460eab34ee1dab1c23f5a3f55e77fbd2600f094658adacd42e00281b8ffb&=&format=webp&quality=lossless)

#### Logo após isso você escolhe como vai se chamar seu Tamagtchi:
![](https://media.discordapp.net/attachments/1194334339954131054/1194712904482693172/image.png?ex=65b15a19&is=659ee519&hm=d1a943d887e066ecb19df5ae55a03ba20eb1d2809cddd01572d45c877fec9f9a&=&format=webp&quality=lossless)

#### Assim que as informações forem passadas o jogo começa: 
![](https://media.discordapp.net/attachments/1194334339954131054/1194713004604932186/image.png?ex=65b15a30&is=659ee530&hm=46fe48b472584117ffe2f64981c375adcf958ac84fb2c5f2da13b1b2fd0a4d8b&=&format=webp&quality=lossless)

## Morte por Felicidade 😀: 

#### Caso a Felicidade do seu Tamagotchi chega a 0%: 
![](https://media.discordapp.net/attachments/1194334339954131054/1194713798729277582/image.png?ex=65b15aee&is=659ee5ee&hm=f6e0c9cf2a667ed4e4fbf7126b7e0473af55d0271435d2a2f6548d94f0c10e85&=&format=webp&quality=lossless)

#### Caso a Felicidade do seu Tamagotchi chega a 100%:
![](https://media.discordapp.net/attachments/1194334339954131054/1194713598010871848/image.png?ex=65b15abe&is=659ee5be&hm=1160a10444c2760b035d1d1c9c9915c9e0e2d2e919edf7c10a268e67a34ceaf6&=&format=webp&quality=lossless)

## Morte por Fome 🍔:

#### Caso a Fome do seu Tamagotchi chegue a 0%:
![](https://media.discordapp.net/attachments/1194334339954131054/1194714023468474438/image.png?ex=65b15b23&is=659ee623&hm=b6e34ab7e7bb80cf4e4d8c279af8b9037edad94d8512442a58d226ab283bbe94&=&format=webp&quality=lossless)

#### Caso a fome do seu Tamagotchi chegue a 110%:
![](https://media.discordapp.net/attachments/1194334339954131054/1194714289274097825/image.png?ex=65b15b63&is=659ee663&hm=71633cb35007d3cbb4a00747f96c68567de2570b0d313c95fc1e9c9b6d9f58f0&=&format=webp&quality=lossless)

## Morte por Energia ⚡:

#### Caso sua Energia chegue a 0%:
![](https://media.discordapp.net/attachments/1194334339954131054/1194714472108011601/image.png?ex=65b15b8e&is=659ee68e&hm=ff724c8b309e860ab88d4ae632220b2198739bb59e546cace9f4a336578e941a&=&format=webp&quality=lossless)

#### Caso sua Energia chegue a 100%:
![](https://media.discordapp.net/attachments/1194334339954131054/1194714640928747530/image.png?ex=65b15bb7&is=659ee6b7&hm=80f696fad89ab037dbfcbbbc0b68f2f1ebfdc91706cb3f0d6fdd87871e5d6e90&=&format=webp&quality=lossless)

#### Caso sua Energia chegue a 110%:
![](https://media.discordapp.net/attachments/1194334339954131054/1194714969485365329/image.png?ex=65b15c05&is=659ee705&hm=966275a7b703cad12ab600b02387059f6022e18725fd13fb3920b3c18ea7f496&=&format=webp&quality=lossless)

## Abandono de Tamagotchi: 

#### Caso você decida sair do jogo você vai estar abandonando seu Tamagotchi💨: 
![](https://media.discordapp.net/attachments/1194334339954131054/1194717134249541652/image.png?ex=65b15e09&is=659ee909&hm=85a69477240cbeb27e67cbf1c7d0a824cd36e2d9acabc3802b3c8e967ddbb0c7&=&format=webp&quality=lossless)

## 👨‍💻 Como rodar o código: 

#### Existem três maneiras de você rodar este código: 

#### 1° - Terminal do Pycharm
#### 2° - Emulador de python  ---- > https://www.online-python.com/#google_vignette
#### 3° - Terminal do Visual Studio Code
