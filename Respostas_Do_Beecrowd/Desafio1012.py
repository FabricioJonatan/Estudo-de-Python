a, b, c = map(input().split(' '))

tri = (a * c)/2
circ = 3.14159 * c ** 2
trap = (a + b)* c / 2
quad = b * b
retang = a * b

print('TRIANGULO: {:.3f}'.format(tri))
print('CIRCULO: {:.3f}'.format(circ))
print('TRAPEZIO: {:.3f}'.format(trap))
print('QUADRADO: {:.3f}'.format(quad))
print('RETANGULO: {:.3f}'.format(retang))