import sys
import random

lista_eleccion = ['piedra', 'papel', 'tijera']

cpu = random.choice(lista_eleccion)
jugador = sys.argv[1].lower()

if jugador == 'piedra' or jugador == 'papel' or jugador == 'tijera':
    print(f'Tu jugaste :{jugador}')
    print(f'Computador jugó :{cpu}')

    if jugador == cpu:
        print('empate')
    elif jugador == 'tijera' and cpu == 'piedra':
        print('perdiste')
    elif jugador == 'tijera' and cpu == 'papel':
        print('ganaste')
    elif jugador == 'piedra' and cpu == 'papel':
        print('perdiste')
    elif jugador == 'piedra' and cpu == 'tijera':
        print('ganaste')
    elif jugador == 'papel' and cpu == 'tijera':
        print('perdiste')
    elif jugador == 'papel' and cpu == 'piedra':
        print('ganaste')
else:
    print('Arguento inválido:  Debe ser piedra, papel o tijera.')