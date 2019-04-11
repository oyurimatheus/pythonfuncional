from collections import Counter
from functools import reduce
import operator
import itertools

from gastos import Gasto


def abre_arquivo(arquivo, encoding='utf-8'):
    with open(arquivo, encoding=encoding) as arquivo:
        tuplas = map(_extrai_tipo_e_valor, arquivo)

        return list(map(Gasto.de_tupla, tuplas))


def previsao(gastos):
    print("calculando previsao...")

    return map(lambda gasto: Gasto(gasto.categoria, gasto.valor + 1), gastos)


def abre_arquivos(arquivos):
    return list(itertools.chain(*map(abre_arquivo, arquivos)))


def prevendo_gastos_de_arquivos(gastos_mensais):
    # gastos_previstos = map(previsao, gastos_mensais)
    gastos_previstos = (previsao(gastos) for gastos in gastos_mensais)
    return list(itertools.chain(*gastos_previstos))


def _extrai_tipo_e_valor(gasto):
    tipo, valor = gasto.split(',')

    return tipo, float(valor)


def total_de_gastos(gastos):
    total = reduce(lambda acumulado, gasto: acumulado + gasto.valor, gastos, 0)

    return total


def categorias_mais_frequentes(gastos):
    categorias = map(operator.attrgetter('categoria'), gastos)
    contador = Counter(categorias)

    categoria_mais_frequente = contador.most_common(n=1)

    return categoria_mais_frequente[0][0]


def total_de_gastos_da_categoria(categoria, gastos):
    gastos_filtrados = filter(lambda gasto: gasto.categoria == categoria, gastos)
    # total = reduce(lambda acumulado, gasto: acumulado + gasto.valor, gastos_filtrados, 0)

    return total_de_gastos(gastos_filtrados)


def gastos_da_categoria(categoria, gastos):
    gastos_filtrados = filter(lambda gasto: gasto.categoria == categoria, gastos)

    for gasto in gastos_filtrados:
        # print('gerando um novo valor')
        yield gasto.valor


def maiores_gastos(gastos):
    return _ordenar_valores(gastos, reverse=True)


def menores_gastos(gastos):
    return _ordenar_valores(gastos)


def _ordenar_valores(gastos, *, reverse=False, top_n=5):
    gastos_ordenados = sorted(gastos, key=operator.attrgetter('valor'), reverse=reverse)
    return gastos_ordenados[:top_n]

