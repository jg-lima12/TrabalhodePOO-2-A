from classes_atv import Aluno
import os
import time

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

aluno = Aluno()

def main():
    while True:
        limpar_terminal()
        escolha_main = int(input('''Qual ação você deseja realizar:
                                
[1]Adicionar Dados
[2]Exibir Dados
[3]Modificar Dado
                                
Resposta: '''))
        if escolha_main == 1:
            limpar_terminal()
            aluno.add_dd()
        elif escolha_main == 2:
            limpar_terminal()
            aluno.exibir_dd()
            input('Pressione ENTER')
        elif escolha_main == 3:
            limpar_terminal()
            aluno.alterar_dd()

main()