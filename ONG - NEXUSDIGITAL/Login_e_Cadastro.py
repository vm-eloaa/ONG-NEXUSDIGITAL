
# Online Python - IDE, Editor, Compiler, Interpreter

# Importa o módulo 'json' que permite trabalhar com dados em formato JSON (JavaScript Object Notation)
# facilita a leitura/gravação de estruturas como listas e dicionários em arquivos.
import json 

# Importa o módulo 'os' para permitir a verificação e manipulação de arquivos e diretórios do sistema operacional.
# No casso desse código ele será ultilizado para verificar se o arquivo de usuários já existe.
import os 

# Nome do arquivo onde os dados dos usuários serão salvos
ARQUIVO_DOS_USUARIOS = 'usuarios.json'

# Se o arquivo não existir, cria um arquivo JSON vazio
if not os.path.exists(ARQUIVO_DOS_USUARIOS):
    # Abre o arquivo no modo 'w' (write = escrita)
    # 'as f' significa que o arquivo aberto será acessado pela variável 'f'
    # json.dump([], f) grava uma lista vazia no arquivo (iniciando os cadastros)
    with open(ARQUIVO_DOS_USUARIOS, 'w') as f:
        json.dump([], f)

# Definindo uma função para carregar os usuários do arquivo JSON criando anteriormente 
def carregar_usuarios():
    # Abre o arquivo no modo 'r' (read = leitura)
    # 'as f' cria uma variável 'f' para manipular o conteúdo do arquivo
    # json.load(f) lê o conteúdo JSON e converte para lista/dicionário Python
    with open(ARQUIVO_DOS_USUARIOS, 'r') as f:
        return json.load(f)

# Função para salvar a lista de usuários no arquivo JSON
def salvar_usuarios(usuarios):
    # Abre o arquivo no modo 'w' (escrita) e sobrescreve o conteúdo
    with open(ARQUIVO_DOS_USUARIOS, 'w') as f:
    # json.dump grava os dados no arquivo com indentação (formatação)
    json.dump(usuarios, f, indent=4) #alinha um 4 espaços

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    print("\n--- CADASTRO DE USUÁRIO ---")
    
    # Solicita os dados do novo usuário
    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    senha = input("Crie uma senha: ")

    # Carrega os usuários que já estão cadastrados
    usuarios = carregar_usuarios()

    # Verifica se o nome já está cadastrado (ultilizando o for)
    for usuario in usuarios:
        if usuario['nome'] == nome :
            print("Usuário já cadastrado!")
            return  # Sai da função sem cadastrar novamente

    # Cria o novo usuário com os determinados dados 
    novo_usuario = {
        'nome': nome,
        'nascimento': nascimento,
        'senha': senha
    }

    # Adiciona o novo usuário à lista
    usuarios.append(novo_usuario) #função append para adicionar a lista

    # Salva a lista atualizada de usuários
    salvar_usuarios(usuarios)

    print("Cadastro realizado com sucesso!")

# Função para o login - somente nome do usuario e senha 
def login():
    print("\n--- LOGIN ---")
    
    # Solicita nome e senha
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")

    # Carregando os usuários que já estão cadastrados
    usuarios = carregar_usuarios()

    # Verifica se o nome e a senha correspondem a algum usuário cadastrado
    for usuario in usuarios:
        if usuario['nome'] == nome and usuario['senha'] == senha: #operador and 
            print("Login realizado com sucesso!")
            return  # Sai da função após login bem-sucedido

    # Se não encontrar o usuário ou senha não corresponder
    print("Nome ou senha incorretos!")

# Função principal com o menu para que o usuário escolha 
def menu():
    while True:
        print("\n===== BEM VINDO(a) a NEXUS DIGITAL =====")
        print("1 - Login")
        print("2 - Cadastrar")
        print("3 - Sair")

        # Solicita a escolha do usuário
        opcao = input("Escolha uma opção: ")

        # Verifica a opção escolhida usando if, elif, else
        if opcao == '1':
            login()
        elif opcao == '2':
            cadastrar()
        elif opcao == '3':
            print("Encerrando o programa.")
            break  # Encerra o laço e sai do programa
        else:
            print("Opção inválida. Tente novamente.")

# Irá inicia o programa chamando o menu principal
menu()
