# crie um programa q leia uma frase qualquer e diga se ela é um palindromo
# palindromo é igual de frente e pra tras

from shlex import join


frase = str(input('Digite uma frase: ')).strip().upper()
juntfrase = ''.join(frase.split())
invfrase = ''.join(reversed(juntfrase))

if juntfrase == invfrase:
    print('Você digitou {}. O seu inverso é {}, logo é um palíndromo.'.format(juntfrase, invfrase))
else:
    print('Você digitou {}. O seu inverso é {}, logo não é um palíndromo.'.format(juntfrase, invfrase))
