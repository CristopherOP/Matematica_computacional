import flet as ft
import mysql.connector

# conexão com o banco de dados

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cris1233!",
        database="universidade"
    )

# funçao para gravar aluno no banco

def gravar_aluno(nome, ra, uc, curso, data_nascimento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO alunos (nome, ra, uc, curso, data_nascimento)
        VALUES (%s, %s, %s, %s, %s)
    """, (nome, ra, uc, curso, data_nascimento))
    conn.commit()
    conn.close()

# interface

def principal(pagina: ft.Page):
    pagina.title = "Cadastro de Alunos"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # campos de entrada
    txt_nome           = ft.TextField(label="Nome")
    txt_ra             = ft.TextField(label="RA")
    txt_uc             = ft.TextField(label="UC")
    txt_curso          = ft.TextField(label="Curso")
    txt_data_nasc      = ft.TextField(label="Data de Nascimento (DD/MM/AAAA)")
    txt_mensagem       = ft.Text("")

    # função do botão de gravar
    def gravar(e):
        try:
            gravar_aluno(
                txt_nome.value,
                txt_ra.value,
                txt_uc.value,
                txt_curso.value,
                txt_data_nasc.value
            )
            txt_mensagem.value = "aluno cadastrado com sucesso!"
            txt_mensagem.color = "green"
            # limpa os campos
            txt_nome.value = ""
            txt_ra.value = ""
            txt_uc.value = ""
            txt_curso.value = ""
            txt_data_nasc.value = ""
        except Exception as erro:
            txt_mensagem.value = f"erro: {erro}"
            txt_mensagem.color = "red"

        pagina.update()

    # botão de gravar
    btn_gravar = ft.ElevatedButton(text="Gravar", on_click=gravar)

    # adiciona os elementos na página
    pagina.add(
        ft.Text("Cadastro de Alunos", size=24, weight=ft.FontWeight.BOLD),
        txt_nome,
        txt_ra,
        txt_uc,
        txt_curso,
        txt_data_nasc,
        btn_gravar,
        txt_mensagem
    )

ft.app(target=principal)