from collections import Counter
from functools import reduce


def abre_arquivo(arquivo, encoding='utf-8'):
    with open(arquivo, encoding=encoding) as arquivo:
        gastos = [_extrai_tipo_e_valor(gasto) for gasto in arquivo]
        return gastos


def _extrai_tipo_e_valor(gasto):
    tipo, valor = gasto.split(',')
    return tipo, float(valor)


def total_de_gastos(gastos):
    total = reduce(lambda acumulado, gasto: acumulado + gasto[1], gastos, 0)

    return total


def categorias_mais_frequentes(gastos):
    categorias = map(lambda gasto: gasto[0], gastos)
    contador = Counter(categorias)

    categoria_mais_frequente = contador.most_common(n=1)

    return categoria_mais_frequente[0][0]


def total_de_gastos_da_categoria(categoria, gastos):
    gastos_filtrados = filter(lambda gasto: gasto[0] == categoria, gastos)
    total = reduce(lambda acumulado, gasto: acumulado + gasto[1], gastos_filtrados, 0)

    return total


def gastos_da_categoria(categoria, gastos):
    gastos_filtrados = filter(lambda gasto: gasto[0] == categoria, gastos)

    for gasto in gastos_filtrados:
        yield gasto[1]


def maiores_gastos(gastos):
    gastos_ordenados = sorted(gastos, key=lambda gasto: gasto[1], reverse=True)
    return gastos_ordenados[:5]


def menores_gastos(gastos):
    gastos_ordenados = sorted(gastos, key=lambda gasto: gasto[1])
    return gastos_ordenados[:5]




