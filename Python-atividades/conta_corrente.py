class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}')
        else:
            print('O valor do depósito deve ser maior que zero.')

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}')
        else:
            print('Valor de saque inválido ou saldo insuficiente.')

conta = ContaCorrente(numero_conta=1553, nome_correntista='Maria')
print(f'Número da conta: {conta.numero_conta}')
print(f'Nome do correntista: {conta.nome_correntista}')
print(f'Saldo inicial: R${conta.saldo:.2f}')

conta.deposito(1000)
conta.saque(500)
conta.alterarNome('Maria Silva')

print(f'Nome atualizado: {conta.nome_correntista}')
