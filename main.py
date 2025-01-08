from classes import Categoria, Despesa, Receita, CalculadoraGastos
from utils import salvar_dados, carregar_dados

def menu():
    print("\n=== Calculadora de Gastos Mensais ===")
    print("1. Adicionar Categoria")
    print("2. Listar Categorias")
    print("3. Adicionar Receita")
    print("4. Adicionar Despesa")
    print("5. Mostrar Saldo")
    print("6. Resumo por Categoria")
    print("7. Definir Limite de Gastos")
    print("8. Verificar Limite de Gastos")
    print("0. Sair")
    return input("Escolha uma opção: ")

def parse_valor(valor_str):
    """
    Tenta converter uma string para float, substituindo vírgulas por pontos, se necessário.
    """
    try:
        return float(valor_str.replace(",", "."))
    except ValueError:
        raise ValueError("Valor inválido. Use apenas números e separadores como ',' ou '.'")

def main():
    calculadora = CalculadoraGastos()

    # Carregar dados ao iniciar o programa
    carregar_dados(calculadora)

    while True:
        opcao = menu()

        if opcao == "1":
            nome_categoria = input("Digite o nome da categoria: ")
            try:
                calculadora.adicionar_categoria(nome_categoria)
                print(f"Categoria '{nome_categoria}' adicionada com sucesso!")
            except ValueError as e:
                print(e)

        elif opcao == "2":
            categorias = calculadora.listar_categorias()
            if categorias:
                print("\nCategorias cadastradas:")
                for categoria in categorias:
                    print(f"- {categoria}")
            else:
                print("Nenhuma categoria cadastrada.")

        elif opcao == "3":
            descricao = input("Digite a descrição da receita: ")
            try:
                valor = parse_valor(input("Digite o valor da receita: "))
                categoria = input("Digite a categoria da receita: ")
                receita = Receita(descricao, valor, categoria)
                calculadora.adicionar_transacao(receita)
                print("Receita adicionada com sucesso!")
            except ValueError as e:
                print(e)

        elif opcao == "4":
            descricao = input("Digite a descrição da despesa: ")
            try:
                valor = parse_valor(input("Digite o valor da despesa: "))
                categoria = input("Digite a categoria da despesa: ")
                despesa = Despesa(descricao, valor, categoria)
                calculadora.adicionar_transacao(despesa)
                print("Despesa adicionada com sucesso!")
            except ValueError as e:
                print(e)

        elif opcao == "5":
            transacoes = calculadora.obter_resumo_por_categoria()
            if not transacoes:
                print("\nNenhuma receita ou despesa registrada.")
            else:
                saldo = calculadora.calcular_saldo()
                print(f"\nSaldo atual: R$ {saldo:.2f}")

        elif opcao == "6":
            resumo = calculadora.obter_resumo_por_categoria()
            if not resumo:
                print("\nNenhuma transação registrada para exibir resumo.")
            else:
                print("\nResumo de gastos por categoria:")
                for categoria, total in resumo.items():
                    print(f"{categoria}: R$ {total:.2f}")

        elif opcao == "7":
            try:
                limite = parse_valor(input("Defina o limite de gastos: "))
                calculadora.definir_limite_gastos(limite)
                print(f"Limite de gastos definido: R$ {limite:.2f}")
            except ValueError as e:
                print(e)

        elif opcao == "8":
            limite = calculadora.definir_limite_gastos if calculadora.verificar_limite() else None
            if limite is None:
                print("\nNenhum limite de gastos definido.")
            elif calculadora.verificar_limite():
                print("\nAlerta! Você ultrapassou o limite de gastos.")
            else:
                print("\nVocê está dentro do limite de gastos.")

        elif opcao == "0":
            print("Saindo do programa...")
            # Salvar dados ao sair do programa
            salvar_dados(calculadora)
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()