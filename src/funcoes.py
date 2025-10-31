def calcularDesc(valor, desc):
    return valor - (valor * desc / 100)

print(f"O kit mouse + teclado logitech de R$190,00 com 5% de desconto ficará {calcularDesc(190, 5):.2f}")


# def calculo(n1, n2):
#     return n1 * n2

# print(f"O resuldado do calculo é de {calculo(10, 5)}")