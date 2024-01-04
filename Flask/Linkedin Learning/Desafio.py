#DESAFIO 1
# estrella1 = 'sol'
# estrella2 = 'Alfa Centauri'
# estrella3 = 'Estrella de barnad'
# estrella4 = 'Luhman 16'

Estrellas = [
    'sol',
    'Alfa Centauri',
    'Estrella de barnad',
    'Luhman 16'
]
print(Estrellas[3])

montanas = {
    'Africana': 'Kilimanjaro',
    'Antartica': 'Macizo Vinson',
    'Indoaustraliana': 'Monte Jaya',
    'Euroasiatica': 'Everest',
    'Norteamerica': 'Monte Denali',
    'Pacifico': 'Volcan Mauna Kea',
    'Suramericana': 'Aconcagua'
}

print(montanas['Pacifico'])

#DESAFIO 2

frutas = [
    'manzanas',
    'bananas',
    'peras',
    'mangos',
    'mandarinas',
    'granadas',
]

print('Nuestra seleccion de frutas')
for fruta in frutas:
    print(fruta)

#Desafio 3
radio = input('Dame el valor del radio del circulo ')
valor_radio = float(radio)
area_circulo = (valor_radio ** 2) * 3.14159
print('El area del circulo es ')
print(area_circulo)