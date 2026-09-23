#biblioteca gráfica para telas
import flet as ft
import mysql.connector as db

import os
import ssl
import certifi

# 1. Configura a variável de ambiente para usar o arquivo do certifi
os.environ['SSL_CERT_FILE'] = certifi.where()

# 2. Cria um contexto que ignora a verificação (Caso o passo 1 falhe em redes corporativas)
ssl._create_default_https_context = ssl._create_unverified_context

def principal(page:ft.Page):
    page.title="Acesso ao sistema"
    page.update()
    
    txt_usuario_cad=ft.TextField(label="Nome do usuário",max_length=15)
    txt_senha_cad=ft.TextField(label="Digite a senha",max_length=10,password=True)
    
    #INSERIR USUÁRIO
    def fechar(e):
        page.open=False

    def insere_usuario(e):
        mca=db.connect(
                host="127.0.0.1",# MESMO QUE LOCALHOST
                user="root",
                password="123456",
                database="mca")
        
        sql="insert into login (usuario,senha) values (%s,%s)"
        valores=(txt_usuario_cad.value,txt_senha_cad.value)
        inserir=mca.cursor()
        inserir.execute(sql,valores)
        mca.commit()
        dialogo=ft.AlertDialog(title="Sucesso",
                              content=[ft.Text("Dados gravados com sucesso.")],
                              actions=[ft.TextButton("Ok")],on_click=fechar,
                              open=True )
        
    #CRIANDO O CADASTRO DE USUÁRIOS
    def cadastra_usuario(e):
        page.clean() #LIMPAR A TELA
        txt_conferesenha_cad=ft.TextField("Confirme a senha",max_length=10)
        btn_gravar=ft.ElevatedButton("Gravar",on_click=insere_usuario)
        btn_cancelar=ft.ElevatedButton("Cancelar",on_click=acesso)
        botoes=ft.Row(controls=[btn_gravar,btn_cancelar])
        page.add(txt_usuario_cad,
                 txt_senha_cad,
                 txt_conferesenha_cad,
                 botoes)
        
    #CRIANDO OBJETOS PARA ENTRADA DE DADOS NO SISTEMA
    def acesso(e):
        #limpar a tela
        page.clean()
        txt_usuario=ft.TextField(
            label="Digite o usuário",
            max_length=15)
        txt_senha=ft.TextField(
            label="Digite a senha",
            max_length=10,
            password=True,
            can_reveal_password=True)
        btn_acessar=ft.ElevatedButton("Acessar")
        btn_sair=ft.ElevatedButton("Sair")
        botoes=ft.Row(controls=[btn_acessar,btn_sair])
        txt_novo=ft.TextButton("Cadastrar Novo",on_click=cadastra_usuario)
        page.add(txt_usuario,
                 txt_senha,botoes,txt_novo)
        page.update()

    #FAZENDO A CHAMADA DO PROCEDIMENTO
    acesso(None)
ft.app(target=principal)