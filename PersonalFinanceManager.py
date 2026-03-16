import json
import os

USER_FILE = "users.json"


def carregar_usuarios():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            return json.load(file)
    return {}


def salvar_usuarios(usuarios):
    with open(USER_FILE, "w") as file:
        json.dump(usuarios, file)


def carregar_dados_usuario(username):
    user_file = f"{username}_data.json"

    if os.path.exists(user_file):
        with open(user_file, "r") as file:
            return json.load(file)

    return {"transacoes": []}


def salvar_dados_usuario(username, dados):
    user_file = f"{username}_data.json"

    with open(user_file, "w") as file:
        json.dump(dados, file)


def criar_usuario(usuarios):
    username = input("Digite um nome de usuário: ")

    if username in usuarios:
        print("Usuário já existe!")
        return usuarios

    password = input("Digite uma senha:")

    usuarios[username] = password

    salvar_usuarios(usuarios)
    salvar_dados_usuario(username, {"transacoes": []})

    print("Usuário criado com sucesso!")

    return usuarios


def login_usuario(usuarios):

    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")

    if usuarios.get(username) == password:

        print("Login bem-sucedido!")

        dados = carregar_dados_usuario(username)

        menu_financeiro(username, dados)

    else:
        print("Usuário ou senha incorretos.")


def adicionar_transacao(username, tipo):

    valor = float(input(f"Digite o valor da {tipo}: "))
    descricao = input("Digite uma descrição: ")

    dados = carregar_dados_usuario(username)

    transacao = {
        "tipo": tipo,
        "valor": valor,
        "descricao": descricao
    }

    dados["transacoes"].append(transacao)

    salvar_dados_usuario(username, dados)

    print(f"{tipo.capitalize()} adicionada com sucesso!")


def ver_historico(username):

    dados = carregar_dados_usuario(username)

    transacoes = dados.get("transacoes", [])

    if not transacoes:
        print("Nenhuma transação registrada.")
        return

    print("\n===== HISTÓRICO =====")

    for i, t in enumerate(transacoes, 1):

        print(
            f"{i}. {t['tipo'].capitalize()} - R${t['valor']} - {t['descricao']}"
        )


def calcular_saldo(username):

    dados = carregar_dados_usuario(username)

    transacoes = dados.get("transacoes", [])

    saldo = sum(
        t["valor"] if t["tipo"] == "receita" else -t["valor"]
        for t in transacoes
    )

    print(f"Saldo atual: R${saldo:.2f}")


def relatorio_por_categoria(username):

    dados = carregar_dados_usuario(username)

    transacoes = dados.get("transacoes", [])

    if not transacoes:
        print("Nenhuma transação registrada.")
        return

    categorias = {}

    total_receitas = 0
    total_despesas = 0

    for t in transacoes:

        categoria = t.get("descricao", "Sem categoria")

        if t["tipo"] == "receita":

            total_receitas += t["valor"]

        else:

            total_despesas += t["valor"]

            categorias[categoria] = categorias.get(categoria, 0) + t["valor"]

    saldo = total_receitas - total_despesas

    print("\n===== RELATÓRIO FINANCEIRO =====")

    print(f"Receitas: R${total_receitas:.2f}")
    print(f"Despesas: R${total_despesas:.2f}")
    print(f"Saldo: R${saldo:.2f}")

    if categorias:

        print("\nGastos por categoria:")

        for cat, valor in categorias.items():
            print(f"- {cat}: R${valor:.2f}")

        top_cat = max(categorias, key=categorias.get)

        print(
            f"\nCategoria que mais gastou: {top_cat} (R${categorias[top_cat]:.2f})"
        )


def menu_financeiro(username, dados):

    while True:

        print("\n====== MENU FINANCEIRO ======")
        print("1 - Adicionar Receita")
        print("2 - Adicionar Despesa")
        print("3 - Ver Histórico")
        print("4 - Calcular Saldo")
        print("5 - Relatório por Categoria")
        print("6 - Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            adicionar_transacao(username, "receita")

        elif choice == "2":
            adicionar_transacao(username, "despesa")

        elif choice == "3":
            ver_historico(username)

        elif choice == "4":
            calcular_saldo(username)

        elif choice == "5":
            relatorio_por_categoria(username)

        elif choice == "6":
            print("Saindo do menu financeiro.")
            break

        else:
            print("Opção inválida!")


def main():

    usuarios = carregar_usuarios()

    while True:

        print("\nBem-vindo ao Personal Finance Manager!")
        print("====== ENTRAR ======")

        print("1 - Login")
        print("2 - Registrar")
        print("3 - Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":

            login_usuario(usuarios)

        elif choice == "2":

            usuarios = criar_usuario(usuarios)

        elif choice == "3":

            print("Encerrando programa...")
            break

        else:

            print("Opção inválida!")


if __name__ == "__main__":
    main()
