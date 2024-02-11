# crie um programa q mostre uma contagem regressiva para estouro de fogos de artificios
# 10 a 0 com intervalo de 1s

import time

print('Contagem Regressiva')
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('Fogos estourando')