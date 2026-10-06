def mostrar_menu():
    print("=== menu ===")
    print("1 - Ver mensagem")
    print("0 - Sair")

def mostrar_mensagem():
    print("bem-vindo")

mostrar_menu ()

opcao = input("escolha: ")

if opcao == "1":
    mostrar_mensagem()
elif opcao == '0':
    print("encerrando...")
else:
    print("Opção inválida!")
