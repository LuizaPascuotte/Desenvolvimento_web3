
def caixinha_magica3(n1, n2):
    resultado = n1 - n2
    if resultado < 0:
        resultado = 0
    return resultado



assert caixinha_magica3(20, 15) == 5
assert caixinha_magica3(20, 10) == 10
assert caixinha_magica3(10, 10) == 0
assert caixinha_magica3(10, 15) == 0
assert caixinha_magica3(30, 45) == 0