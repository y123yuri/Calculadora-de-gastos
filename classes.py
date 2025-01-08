from datetime import datetime

class Categoria:
    def __init__(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        if not novo_nome.strip():
            raise ValueError("O nome da categoria não pode ser vazio.")
        self._nome = novo_nome


class Transacao:
    def __init__(self, descricao, valor, categoria):
        self._descricao = descricao
        self._valor = valor
        self._categoria = categoria
        self._data = datetime.now()

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, nova_descricao):
        if not nova_descricao.strip():
            raise ValueError("A descrição não pode ser vazia.")
        self._descricao = nova_descricao

    def get_valor(self):
        return self._valor

    def set_valor(self, novo_valor):
        if novo_valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")
        self._valor = novo_valor

    def get_categoria(self):
        return self._categoria

    def get_data(self):
        return self._data


class Despesa(Transacao):
    def __init__(self, descricao, valor, categoria):
        super().__init__(descricao, valor, categoria)


class Receita(Transacao):
    def __init__(self, descricao, valor, categoria):
        super().__init__(descricao, valor, categoria)


class CalculadoraGastos:
    def __init__(self):
        self._categorias = []
        self._transacoes = []
        self._limite_gastos = None
    
    def obter_transacoes(self):
        return self._transacoes


    def adicionar_categoria(self, nome_categoria):
        if any(c.get_nome() == nome_categoria for c in self._categorias):
            raise ValueError("Categoria já existe.")
        self._categorias.append(Categoria(nome_categoria))

    def listar_categorias(self):
        return [categoria.get_nome() for categoria in self._categorias]

    def adicionar_transacao(self, transacao):
        if not isinstance(transacao, Transacao):
            raise ValueError("Objeto deve ser uma instância de Transacao.")
        self._transacoes.append(transacao)

    def calcular_saldo(self):
        receitas = sum(t.get_valor() for t in self._transacoes if isinstance(t, Receita))
        despesas = sum(t.get_valor() for t in self._transacoes if isinstance(t, Despesa))
        return receitas - despesas

    def verificar_limite(self):
        if self._limite_gastos is not None:
            total_despesas = sum(t.get_valor() for t in self._transacoes if isinstance(t, Despesa))
            return total_despesas > self._limite_gastos
        return False

    def definir_limite_gastos(self, limite):
        if limite <= 0:
            raise ValueError("O limite de gastos deve ser maior que zero.")
        self._limite_gastos = limite

    def obter_resumo_por_categoria(self):
        resumo = {}
        for categoria in self._categorias:
            total = sum(
                t.get_valor()
                for t in self._transacoes
                if t.get_categoria() == categoria.get_nome() and isinstance(t, Despesa)
            )
            resumo[categoria.get_nome()] = total
        return resumo
