import gerenciador_de_gastos
import menu_ui

arquivo = input('Digite o nome do arquivo que deseja abrir: ')
gastos = gerenciador_de_gastos.abre_arquivo(arquivo)

menu_ui.mostra_menu(gastos)
