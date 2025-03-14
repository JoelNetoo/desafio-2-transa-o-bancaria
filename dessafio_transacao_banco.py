menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastrar Novo Usuário
[q] Sair

=> """

# Inicialização dos dados
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Dicionário para armazenar dados dos usuários
usuarios = {}

# Função para cadastrar novo usuário
def cadastrar_usuario():
    print("\n=== Cadastro de Novo Usuário ===")
    nome = input("Nome completo: ")
    cpf = input("CPF (somente números): ")
    endereco = input("Endereço: ")
    agencia = input("Agência: ")
    tipo_conta = input("Tipo de conta (ex: 0001): ")
    
    # Verificar se o CPF já existe no sistema
    if cpf in usuarios:
        print("\nEste CPF já está cadastrado.")
    else:
        usuarios[cpf] = {
            "nome": nome,
            "cpf": cpf,
            "endereco": endereco,
            "agencia": agencia,
            "tipo_conta": tipo_conta,
            "saldo": saldo,
            "extrato": "",
            "numero_saques": numero_saques
        }
        print("\nUsuário cadastrado com sucesso!")

# Função para mostrar o extrato de um usuário
def mostrar_extrato(cpf):
    usuario = usuarios[cpf]
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not usuario["extrato"] else usuario["extrato"])
    print(f"\nSaldo: R$ {usuario['saldo']:.2f}")
    print("==========================================")

# Função para realizar um depósito
def depositar(cpf, valor):
    usuario = usuarios[cpf]
    if valor > 0:
        usuario["saldo"] += valor
        usuario["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para realizar um saque
def sacar(cpf, valor):
    usuario = usuarios[cpf]
    
    excedeu_saldo = valor > usuario["saldo"]
    excedeu_limite = valor > limite
    excedeu_saques = usuario["numero_saques"] >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        usuario["saldo"] -= valor
        usuario["extrato"] += f"Saque: R$ {valor:.2f}\n"
        usuario["numero_saques"] += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para verificar se o usuário existe
def verificar_usuario(cpf):
    if cpf not in usuarios:
        print("Usuário não encontrado. Cadastre-se antes de realizar qualquer operação.")
        return False
    return True

# Função principal
while True:
    opcao = input(menu)

    if opcao == "u":
        cadastrar_usuario()

    elif opcao == "d":
        cpf = input("Informe o CPF: ")
        if verificar_usuario(cpf):
            valor = float(input("Informe o valor do depósito: "))
            depositar(cpf, valor)

    elif opcao == "s":
        cpf = input("Informe o CPF: ")
        if verificar_usuario(cpf):
            valor = float(input("Informe o valor do saque: "))
            sacar(cpf, valor)

    elif opcao == "e":
        cpf = input("Informe o CPF: ")
        if verificar_usuario(cpf):
            mostrar_extrato(cpf)

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
 