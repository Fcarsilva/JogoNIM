
def computador_escolhe_jogada(n, m):    
    print("\nComputador começa!\n")
    if n <= m:
        return n
    else:
        if n % (m+1) > 0:
            return n % (m+1)
        return m


def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada ==0:
        jogada = int(input("Quantas peças você vai tirar? "))
        print("\n Oops! Jogada inválida! Tente de novo.\n")
        if jogada > n or jogada < 1 or jogada > m:
            jogada = 0
           
    return jogada



def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while m < 1:
        print("A quantidade de peças por jogadas devem ser menor ou igual as peças totais")
        m = int(input("Limite de peças por jogada? "))
    
    valor = 0
    jogada = 0
    if (n % (m+1)) == 0:
        print("\nVocê começa!")
        jogada = 1 
        while n > 0:
            if jogada == 1:
                valor = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", valor, "peça(s).")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 2
            else:
                valor = computador_escolhe_jogada(n, m)
                print("\nO computador tirou", valor, "peça(s)")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 1
                
        if jogada == 1:
            print("Fim do jogo! O computador ganhou!\n")
            return 2 
        else:
            print("Fim do jogo! O você ganhou!\n")
            return 1 
                
    else:
        print("\nComputador começa!")
        jogada = 2 
        while n > 0:
            if jogada == 2:
                valor = computador_escolhe_jogada(n, m)
                print("\nO computador tirou", valor, "peça(s)")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 1
            else:
                valor = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", valor, "peça(s).")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 2
                
        if jogada == 1:
            print("Fim do jogo! O computador ganhou!\n")
            return 2 
        else:
            print("Fim do jogo! O você ganhou!\n")
            return 1 
    

def campeonato():

    
    usuario = 0
    computador = 0

    
    for _ in range(3):

        
        vencedor = partida()

        
        if vencedor == 1:
            
            usuario = usuario + 1
        else:
            
            computador = computador + 1

    
    print("Placar final: Você  {} x {}  Computador".format(usuario, computador))
        
opçãodejogo = 0
while opçãodejogo == 0:

    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato ")

    opçãodejogo = int(input("Escolha:"))
    if opçãodejogo == 1:
        print("Você escolheu uma partida isolada!")
        partida()
        break
    elif opçãodejogo == 2:
        print("Você escolheu um campeonato!")
        campeonato()
        break
    else:
        print("Opão Inválida!")
        opçãodejogo = 0
        
    
       
