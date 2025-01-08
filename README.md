# Calculadora de Gastos Mensais

**Calculadora de Gastos Mensais** é um projeto Python que permite gerenciar receitas e despesas, categorizá-las e monitorar o saldo financeiro de maneira simples e eficiente.

## Funcionalidades

1. **Gerenciamento de Categorias:**
   - Adicione categorias personalizadas como `Alimentação`, `Transporte`, `Lazer`, entre outras.
   - Liste todas as categorias cadastradas.

2. **Gerenciamento de Transações:**
   - Cadastre receitas e despesas associando-as a categorias específicas.
   - Exiba o saldo atual baseado nas receitas e despesas registradas.

3. **Resumo Financeiro:**
   - Visualize o resumo de gastos por categoria.
   - Exporte os dados financeiros para arquivos JSON.

4. **Controle de Limites:**
   - Defina um limite de gastos e receba alertas se o limite for ultrapassado.

5. **Persistência de Dados:**
   - As informações de categorias e transações são salvas automaticamente em arquivos JSON ao sair do programa.
   - Os dados são carregados automaticamente ao iniciar.

---

## Estrutura do Projeto

```plaintext
calculadora_gastos/
├── main.py                 # Arquivo principal, responsável pela interação com o usuário.
├── classes.py              # Classes principais do sistema (Categoria, Receita, Despesa, CalculadoraGastos).
├── utils.py                # Funções auxiliares para salvar e carregar dados.
├── data/                   # Diretório para armazenar os dados persistentes.
│   ├── categorias.json     # Arquivo JSON para as categorias cadastradas.
│   ├── transacoes.json     # Arquivo JSON para as transações registradas.
├── tests/                  # Testes unitários (em desenvolvimento).
├── README.md               # Documentação do projeto.
└── requirements.txt        # Lista de dependências (se aplicável).
```

---

## Como Executar

### Pré-requisitos
- Python 3.7 ou superior.

### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/calculadora-gastos.git
   cd calculadora-gastos
   ```

2. Execute o programa:
   ```bash
   python main.py
   ```

---

## Uso

1. Ao iniciar o programa, um menu será exibido com as seguintes opções:
   - Adicionar categorias, receitas e despesas.
   - Visualizar saldo e resumo por categoria.
   - Definir limites de gastos e verificar alertas.

2. Ao sair do programa, os dados serão salvos automaticamente.

