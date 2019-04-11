import gerenciador_de_gastos


def mostra_menu(gastos):
    texto_do_menu = '''
OPÇÕES

1 - Total dos gastos
2 - Gastos mais frequentes
3 - Total de gastos de uma categoria
4 - Lista de gastos de uma categoria
5 - Listar os 5 maiores gastos
6 - Listar os 5 menores gastos
7 - Previsão dos gastos do próximo mês
0 - Sair do programa
'''

    opcoes = {
        1: mostra_total_gastos,
        2: mostra_gastos_frequentes,
        3: mostra_total_de_gasto_da_categoria,
        4: mostra_lista_de_gastos_da_categoria,
        5: mostra_5_maiores_gastos,
        6: mostra_5_menores_gastos,
        7: previsao_de_gastos

    }

    while True:
        print(texto_do_menu)
        opcao = int(input('Selecione uma opção: '))

        while opcao < 0 or opcao > 7:
            opcao = int(input('Selecione uma opção válida: '))

        if opcao == 0:
            break

        funcao = opcoes.get(opcao)
        executa_opcao(funcao, gastos)


def executa_opcao(funcao, gastos):
    funcao(gastos)


def mostra_lista_de_gastos_da_categoria(gastos):
    categoria = input('Digite o nome da categoria: ')
    gastos_da_categoria = gerenciador_de_gastos.gastos_da_categoria(categoria, gastos)
    print(f'Os gastos da categoria {categoria} foram:')
    for gasto in gastos_da_categoria:
        print(f'\t - R${gasto}')


def mostra_total_de_gasto_da_categoria(gastos):
    categoria = input('Digite o nome da categoria: ')
    gastos_da_categoria = gerenciador_de_gastos.total_de_gastos_da_categoria(categoria, gastos)
    print(f'O total de gastos da categoria {categoria} foi de {gastos_da_categoria}')


def mostra_gastos_frequentes(gastos):
    mais_frequente = gerenciador_de_gastos.categorias_mais_frequentes(gastos)
    print(f'A categoria mais frequente foi a {mais_frequente}')


def mostra_total_gastos(gastos):
    total = gerenciador_de_gastos.total_de_gastos(gastos)
    print(f'Os gastos totais foram de R$ {total}')


def mostra_5_maiores_gastos(gastos):
    maiores_gastos = gerenciador_de_gastos.maiores_gastos(gastos)
    print('Os maiores gastos foram:')
    for gasto in maiores_gastos:
        print(f'{gasto.categoria} - R$ {gasto.valor}')


def mostra_5_menores_gastos(gastos):
    menores_gastos = gerenciador_de_gastos.menores_gastos(gastos)
    print('Os menores gastos foram:')
    for gasto in menores_gastos:
        print(f'{gasto.categoria} - R$ {gasto.valor}')


def previsao_de_gastos(gastos):
    lista_de_gastos = [gastos]
    arquivo = input('Se desejar abrir outro arquivo, digite seu nome, senão pressione <Enter>: ')
    if arquivo:
        lista_de_gastos.append(gerenciador_de_gastos.abre_arquivo(arquivo))

    gastos_previstos = gerenciador_de_gastos.prevendo_gastos_de_arquivos(lista_de_gastos)

    print(f'Listando {len(gastos_previstos)} gastos')
    for gasto in gastos_previstos:
        print(f'{gasto.categoria} - R$ {gasto.valor}')
