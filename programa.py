import random

while True:
    aleatorio = random.randrange(0, 3)
    maquina = ""
    print('1. Piedra\n')
    print('2. Papel\n')
    print('3. Tijera\n')

    opcion = int(input('Elije tu opcion: '))

    if opcion == 1:
        usuario = 'Piedra'
    elif opcion == 2:
        usuario = 'Papel'
    elif opcion == 3:
        usuario = 'Tijera'
    print(f'Elejiste: {usuario}')

    if aleatorio == 0:
        maquina = 'Piedra'
    elif aleatorio == 1:
        maquina = 'Papel'
    elif aleatorio == 2:
        maquina = 'Tijera'
    print(f'La maquina elijio: {maquina}\n')
    print('....\n')

    if maquina == 'Piedra' and usuario == 'Papel':
        print('Ganaste, papel envuelve a piedra.\n')
    elif maquina == 'Papel' and usuario == 'Tijera':
        print('Ganaste, tijera corta el papel.\n')
    elif maquina == 'Tijera' and usuario == 'Piedra':
        print('Ganaste, piedra rompe tijera.\n')
    elif maquina == 'Papel' and usuario == 'Piedra':
        print('Perdiste, papel envuelve piedra.\n')
    elif maquina == 'Tijera' and usuario == 'Papel':
        print('Perdiste, tijera corta papel.\n')
    elif maquina == 'Piedra' and usuario == 'Tijera':
        print('Perdiste, piedra rompe tijera.\n')
    elif maquina == usuario:
        print('Empate...\n')