# import qrcode

# def create_QRCode():
#     chapa = input("insira a chapa do funcionario: ")
#     nome = input("Insira o nome do funcionario: ")
#     contador = input("insira a quantidade de usos: ")
#     dados = "Chapa: " + chapa + " Nome: " + nome  + " Quantidade de usos: " + contador
#     qr = qrcode.make(dados)  
#     qr.save(f"./QRCode/{chapa}.png")  
#     print(f"QRCode gerado e salvo como {chapa}.png")


# create_QRCode()

import sqlite3

def create_table():

    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        chapa TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        contador INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def insert_data(chapa, nome, contador):

    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO funcionarios (chapa, nome, contador)
    VALUES (?, ?, ?)
    ''', (chapa, nome, contador))
    conn.commit()
    conn.close()

def create_new_employee():
  
    chapa = input("Insira a chapa do funcionário: ")
    nome = input("Insira o nome do funcionário: ")
    contador = input("Insira a quantidade de usos: ")

    if not contador.isdigit():
        print("Por favor, insira um número válido para a quantidade de usos.")
        return
    
    contador = int(contador)

    
    insert_data(chapa, nome, contador)
    print(f"Cadastro de {nome} com chapa {chapa} foi salvo no banco de dados com {contador} usos.")

def add_usage_to_employee():
   
    chapa = input("Insira a chapa do funcionário para adicionar usos: ")


    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()


    cursor.execute('SELECT * FROM funcionarios WHERE chapa = ?', (chapa,))
    result = cursor.fetchone()

    if result:
        nome, contador = result[1], result[2]

        adicionar = input(f"O funcionário {nome} tem {contador} usos restantes. Quantos usos deseja adicionar? ")
        
        if not adicionar.isdigit():
            print("Por favor, insira um número válido de usos a adicionar.")
            conn.close()
            return

        adicionar = int(adicionar)
        contador += adicionar

        insert_data(chapa, nome, contador)
        print(f"Contador de {nome} (chapa {chapa}) atualizado para {contador} usos.")
    else:
        print(f"Funcionário com chapa {chapa} não encontrado.")
    
    conn.close()

def main_menu():

    while True:
        print("\nEscolha uma opção:")
        print("1 - Criar novo cadastro de funcionário")
        print("2 - Adicionar usos a um contador de funcionário")
        print("3 - Sair")
        
        escolha = input("Digite sua escolha (1/2/3): ")

        if escolha == '1':
            create_new_employee()
        elif escolha == '2':
            add_usage_to_employee()
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


create_table()


main_menu()

