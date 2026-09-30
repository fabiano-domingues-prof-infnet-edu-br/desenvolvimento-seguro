import sqlite3
import subprocess

DB_PASSWORD = "super_secret_password_123"

def buscar_usuario(nome_usuario):
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()
    
    query = f"SELECT * FROM usuarios WHERE nome = '{nome_usuario}'"
    
    cursor.execute(query)
    return cursor.fetchall()


def pingar_servidor(ip_usuario):
    comando = f"ping -c 4 {ip_usuario}"
    
    subprocess.call(comando, shell=True)
