from collections import Counter


def abre_arquivo(arquivo, encoding='utf-8'):
    with open(arquivo, encoding=encoding) as arquivo:
        gastos = [_extrai_tipo_e_valor(gasto) for gasto in arquivo]
        return gastos


def _extrai_tipo_e_valor(gasto):
    tipo, valor = gasto.split(',')
    return tipo, float(valor)


def total_de_gastos(gastos):
    total = 0
    for _, valor in gastos:
        total += valor

    return total


def total_de_gastos_da_categoria(categoria, gastos):
    total = 0
    for gasto in gastos:
        if categoria == gasto[0]:
            total += gasto[1]
    return total


def gastos_da_categoria(categoria, gastos):
    return [gasto[1] for gasto in gastos if gasto[0] == categoria]


def categorias_mais_frequentes(gastos):
    categorias = [gasto[0] for gasto in gastos]
    contador = Counter(categorias)

    categoria_mais_frequente = contador.most_common(n=1)

    return categoria_mais_frequente[0][0]



