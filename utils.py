import json
from classes import Despesa, Receita

def salvar_dados(calculadora, categorias_path='data/categorias.json', transacoes_path='data/transacoes.json'):
    """
    Salva categorias e transações em arquivos JSON.
    """
    try:
        # Salvar categorias
        categorias = calculadora.listar_categorias()
        with open(categorias_path, 'w') as cat_file:
            json.dump(categorias, cat_file)

        # Salvar transações
        transacoes = []
        for transacao in calculadora.obter_transacoes():
            transacoes.append({
                "descricao": transacao.get_descricao(),
                "valor": transacao.get_valor(),
                "categoria": transacao.get_categoria(),
                "tipo": "Receita" if isinstance(transacao, Receita) else "Despesa"
            })
        with open(transacoes_path, 'w') as trans_file:
            json.dump(transacoes, trans_file)

    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def carregar_dados(calculadora, categorias_path='data/categorias.json', transacoes_path='data/transacoes.json'):
    """
    Carrega categorias e transações de arquivos JSON.
    """
    try:
        # Carregar categorias
        with open(categorias_path, 'r') as cat_file:
            categorias = json.load(cat_file)
            for nome in categorias:
                calculadora.adicionar_categoria(nome)

        # Carregar transações
        with open(transacoes_path, 'r') as trans_file:
            transacoes = json.load(trans_file)
            for t in transacoes:
                if t['tipo'] == 'Receita':
                    transacao = Receita(t['descricao'], t['valor'], t['categoria'])
                else:
                    transacao = Despesa(t['descricao'], t['valor'], t['categoria'])
                calculadora.adicionar_transacao(transacao)

    except FileNotFoundError:
        print("Arquivos de dados não encontrados. Iniciando com dados vazios.")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
