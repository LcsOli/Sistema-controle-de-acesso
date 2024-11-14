
import sqlite3

def use_QRCode():
   
    chapa = input("Insira a chapa do funcionário: ")


    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM funcionarios WHERE chapa = ?', (chapa,))
    result = cursor.fetchone()
      
    if result:
        nome, contador = result[1], result[2]

        
        if contador > 0:
           
            contador -= 1

           
            cursor.execute('UPDATE funcionarios SET contador = ? WHERE chapa = ?', (contador, chapa))
            conn.commit()

            print(f"Uso realizado para {nome}. Contador agora é: {contador}")
        else:
            print(f"Não há mais usos disponíveis para o funcionário {nome}.")
    else:
        print("Chapa não encontrada no banco de dados.")

    conn.close()

use_QRCode()
