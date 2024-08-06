print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo.')
    if r1 == r2 == r3:
        print('Este triângulo é equilátero, pois todos os segmentos são iguais.')
    elif r1 != r2 != r3 != r1:
        print('Este triângulo é escaleno, pois possui dois lados iguais.')
    else:
        print('Este triângulo é isóceles, pois todos os lados são diferentes.')
else:
    print('Os segmentos acima não podem formar um triângulo.')