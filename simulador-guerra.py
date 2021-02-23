import random

palos = ['Espada', 'Basto', 'Oro', 'Copa']
valores = ['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Sota', 'Caballero', 'Rey']
numeros = {'Uno': 1, 'Dos': 2, 'Tres': 3, 'Cuatro': 4, 'Cinco': 5, 'Seis': 6, 'Siete': 7, 'Ocho': 8, 'Nueve': 9, 'Sota': 10, 'Caballero': 11, 'Rey': 12}

class Carta:
    def __init__(self, palo, valor):
        self.valor = valor
        self.palo = palo
        self.numero = numeros[valor]

    def __str__(self):
        return '{} de {}'.format(self.valor, self.palo)

class Mazo:
    def __init__(self):
        self.cartas = []
        for palo in palos:
            for valor in valores:
                self.cartas.append(Carta(palo, valor))

    def mezclar(self):
        random.shuffle(self.cartas)

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ejercito = []

    def sacar_una(self):
        return self.ejercito.pop(0)

    def agregar_cartas(self, nuevas):
        if type(nuevas) == type([]):
            self.ejercito.extend(nuevas)
        else:
            self.ejercito.append(nuevas)

    def __str__(self):
        return '{} tiene {} cartas en su ejército'.format(self.nombre, len(self.ejercito))

ronda = 0

j1 = Jugador('Jugador 1')
j2 = Jugador('Jugador 2')
j1_mano = []
j2_mano = []

mazo = Mazo()
mazo.mezclar()
j1.agregar_cartas(mazo.cartas[:int(len(mazo.cartas)/2)])
j2.agregar_cartas(mazo.cartas[int(len(mazo.cartas)/2):])

while True:
    ronda += 1
    print(f'Ronda {ronda}')

    #Verifica si tienen cartas para seguir jugando
    if len(j1.ejercito) == 0:
        print('{} se quedó sin ejército. {} ganó la partida!'.format(j1.nombre, j2.nombre))
        break
    elif len(j2.ejercito) == 0:
        print('{} se quedó sin ejército. {} ganó la partida!'.format(j2.nombre, j1.nombre))
        break

    #Agrega carta a la mano
    j1_mano.append(j1.sacar_una())
    print('::::J1::{}'.format(j1_mano[-1]))
    j2_mano.append(j2.sacar_una())
    print('::::J2::{}'.format(j2_mano[-1]))

    #Condición de victoria
    if j1_mano[-1].numero > j2_mano[-1].numero:
        j1.agregar_cartas(j1_mano)
        j1.agregar_cartas(j2_mano)
        j1_mano = []
        j2_mano = []
        print(':::::::J1 ganó la ronda:::::::')
    elif j2_mano[-1].numero > j1_mano[-1].numero:
        j2.agregar_cartas(j2_mano)
        j2.agregar_cartas(j1_mano)
        j1_mano = []
        j2_mano = []
        print(':::::::J2 ganó la ronda:::::::')
    elif j1_mano[-1].numero == j2_mano[-1].numero:
        print('------------GUERRA------------')
        if len(j1.ejercito) < 6 and len(j2.ejercito) > 5:
            print('{} no tiene ejército suficiente para pelear la guerra. {} ganó la partida!'.format(j1.nombre, j2.nombre))
            break
        elif len(j2.ejercito) < 6 and len(j1.ejercito) > 6:
            print('{} no tiene ejército suficiente para pelear la guerra. {} ganó la partida!'.format(j1.nombre, j2.nombre))
            break
        elif len(j1.ejercito) < 6 and len(j2.ejercito) < 6:
            print('{} y {} no tienen suficiente ejército para pelear la guerra. Ambos jugadores perdieron la partida'.format(j1.nombre, j2.nombre))
            break
        else:
            for cant in range(5):
                j1_mano.append(j1.sacar_una())
                j2_mano.append(j2.sacar_una())