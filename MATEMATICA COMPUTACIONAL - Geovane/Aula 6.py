#------------------------------------------------------
# Autor: NOME DA PESSOA
# Ultima alteração: 04/05/2026
#------------------------------------------------------

#Biblioteca para uso de objetos com janelas 
import flet as ft
#Biblioteca de geração de gráficos para as funções etc..
import matplotlib as plt
#Biblioteca para operações mátemáticas e matrizes diversas
import numpy as nu
#Biblioteca para uso de operações de sistema
import sys 
# Definindo a rotina principal
#-------------------------------------------------------------------
def main(pagina:ft.Page): #função principal do sistema
     #Coloca o título na janela do aplicativo
     pagina.title="Exemplo de uso da Barra de Menu"
     #-------------------------------------
     #procedimento para sair da aplicação
     #-------------------------------------
     def sair_app(e):
         sys.exit() 
     pagina.appbar=ft.AppBar(
          leading=ft.Icon("Menu"),#DEFINE O ÍCONE DO MENU
          title="Menu Principal", #TITULO DO MENU
          bgcolor=ft.Colors.BLUE_700, #COR DE FUNDO
          actions=[ #DEFINIE AS AÇÕES DO MENU 
               ft.PopupMenuButton(
                   items=[ #ADICIONAR OS ITENS PAR O MENU POPUP
                        
                        ft.PopupMenuItem("Opção 1",ft.IconButton(ft.Icons.SETTINGS,icon_size=50,icon_color="Red")), #DEFININDO ÍCONE PARA A OPÇÃO
                        ft.PopupMenuItem("Opcao 2"),
                        ft.PopupMenuItem("Opção 3"),
                        ft.Divider(), # CRIAR UM DIVISOR PARA O MENU
                        ft.PopupMenuItem("Sair",on_click=sair_app) #CHAMADA DA FUNÇÃO NO EVENTO ON_CLICK
                 ]) 
            ]      
     )
     #-------------------------------------
     #Atualizar para visualizar as modificações feitas na janela
     pagina.update()
ft.app(target=main)
#Fim da aplicação
#-------------------------------------------------------------------