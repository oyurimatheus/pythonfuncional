import gerenciador_de_gastos


def menu(gastos):
    texto_do_menu = '''
OPÇÕES

1 - Total dos gastos
2 - Gastos mais frequentes
3 - Total de gastos de uma categoria
4 - Lista de gastos de uma categoria
5 - Maiores gastos
6 - Menores gastos
0 - Sair do programa
'''

    while True:
        print(texto_do_menu)
        opcao = int(input('Selecione uma opção: '))

        while opcao < 0 or opcao > 6:
            opcao = int(input('Selecione uma opção válida: '))

        if opcao == 1:
            total = gerenciador_de_gastos.total_de_gastos(gastos)
            print(f'Os gastos totais foram de R${total}')

        elif opcao == 2:

            mais_frequente = gerenciador_de_gastos.categorias_mais_frequentes(gastos)
            print(f'A categoria mais frequente foi a {mais_frequente}')

        elif opcao == 3:
            categoria = input('Digite o nome da categoria: ')
            gastos_da_categoria = gerenciador_de_gastos.total_de_gastos_da_categoria(categoria, gastos)
            print(f'O total de gastos da categoria {categoria} foi de {gastos_da_categoria}')

        elif opcao == 4:
            categoria = input('Digite o nome da categoria: ')
            gastos_da_categoria = gerenciador_de_gastos.gastos_da_categoria(categoria, gastos)
            print(f'Os gastos da categoria {categoria} foram:')
            for gasto in gastos_da_categoria:
                print(f'\t{gasto}')

        elif opcao == 5:
            maiores_gastos = gerenciador_de_gastos.maiores_gastos(gastos)
            print('Os maiores gastos foram:')
            for gasto in maiores_gastos:
                print(f'{gasto[0]} - R${gasto[1]}')

        elif opcao == 6:
            menores_gastos = gerenciador_de_gastos.menores_gastos(gastos)
            print('Os menores gastos foram:')
            for gasto in menores_gastos:
                print(f'{gasto[0]} - R${gasto[1]}')

        else:
            break


if __name__ == '__main__':
    arquivo = input('Digite o nome do arquivo que deseja abrir: ')
    gastos = gerenciador_de_gastos.abre_arquivo(arquivo)

    menu(gastos)
