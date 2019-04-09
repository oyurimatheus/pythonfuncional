from collections import Counter
from functools import reduce

from gastos import Gasto


def abre_arquivo(arquivo, encoding='utf-8'):
    with open(arquivo, encoding=encoding) as arquivo:
        gastos = [_extrai_tipo_e_valor(gasto) for gasto in arquivo]
        return gastos


def _extrai_tipo_e_valor(gasto):
    tipo, valor = gasto.split(',')

    return Gasto(tipo, float(valor))


def total_de_gastos(gastos):
    total = reduce(lambda acumulado, gasto: acumulado + gasto.valor, gastos, 0)

    return total


def categorias_mais_frequentes(gastos):
    categorias = map(lambda gasto: gasto[0], gastos)
    contador = Counter(categorias)

    categoria_mais_frequente = contador.most_common(n=1)

    return categoria_mais_frequente[0][0]


def total_de_gastos_da_categoria(categoria, gastos):
    gastos_filtrados = filter(lambda gasto: gasto.categoria == categoria, gastos)
    total = reduce(lambda acumulado, gasto: acumulado + gasto.valor, gastos_filtrados, 0)

    return total


def gastos_da_categoria(categoria, gastos):
    gastos_filtrados = filter(lambda gasto: gasto.categoria == categoria, gastos)

    for gasto in gastos_filtrados:
        yield gasto[1]


def maiores_gastos(gastos):
    return _ordenar_valores(gastos, reverse=True)


def menores_gastos(gastos):
    return  _ordenar_valores(gastos)


def _ordenar_valores(gastos, *, reverse=False, top=5):
    gastos_ordenados = sorted(gastos, key=lambda gasto: gasto.categoria, reverse=reverse)
    return gastos_ordenados[:top]

