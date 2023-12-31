#  Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
vitoria = 0

while True:
    jogador = int(input('Digite um número: '))
    computador = random.randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
      tipo = str(input('Par ou ímpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador} . Total de {total} = ' , end= '')
    print('PAR' if total % 2 == 0 else 'IMPAR' )
  
    if tipo == 'P':
       if total % 2 == 0:
          print('Você VENCEU ! ')
          vitoria += 1

       else:
          print('Você PERDEU ')
          break
          
    elif tipo == 'I':
       if total % 2 == 1:
          print('Você VENCEU !')
          vitoria += 1
       else:
          print('Você PERDEU')
          break

    print('Vamos jogar novamente...')

print(f'Game Over ! Você ganhou {vitoria} vezes' )