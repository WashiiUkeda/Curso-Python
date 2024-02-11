# Criar um programa que leia um nome completo de uma pessoa e mostre
# * Todas minusculas
# * Todas maiusculas
# * Quantas letras ao todo sem considerar espaço
# * Quantas letras tem o primeiro nome

name = str(input("Informe seu nome completo: ")).strip
tam = len(name)
tamEsp = tam - name.count(" ")

print('Nome em minuscula: {}\n'
      'Nome em maíscula: {}\n'
      'O seu nome tem {} letras desconsiderando os espaços \n'
      'e o primeiro nome tem {} letras.'.format(name.lower(), name.upper(), tamEsp, len(name.split()[0])))
