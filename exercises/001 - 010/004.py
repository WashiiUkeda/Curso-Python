#Criar um programa que leia um valor e disseque ele

valor = input("Digite algo: ")

print("É Alfanumérico? ", valor.isalnum())
print("É alfabético? ", valor.isalpha())
print("É numérico? ", valor.isnumeric())
print("Só tem maiusculas? ", valor.isupper())
print("É decimal? ", valor.isdecimal())
print("Só tem minusculas? ", valor.islower())
