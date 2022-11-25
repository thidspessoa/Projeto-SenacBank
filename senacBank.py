# Conta Corrente
class ContaCorrente:
    def __init__(self, nome_do_titular, numero_conta, saldo_corrente, saldo_poupanca, senha) -> None:
        self.nome_do_titular = nome_do_titular
        self.numero_conta = numero_conta
        self.__saldo_corrente = saldo_corrente
        self.__saldo_poupanca = saldo_poupanca
        self.senha = senha

    # Pega o saldo atual da conta corrente
    def get_saldo_corrente(self) -> float:
        return self.__saldo_corrente

    # Muda o saldo atual da conta corrente
    def set_saldo_corrente(self, operador, valor) -> None:

        if operador == '+':
            self.__saldo_corrente += valor

        elif operador == '-':
            self.__saldo_corrente -= valor

        else:
            return print('Operador inválido')
        # Pega o saldo atual da conta poupanca

    def get_saldo_poupanca(self) -> float:
        return self.__saldo_poupanca

        # Muda o saldo atual da conta poupanca

    def set_saldo_poupanca(self, operador, valor) -> None:

        if operador == '+':
            self.__saldo_poupanca += valor

        elif operador == '-':
            self.__saldo_poupanca -= valor

        else:
            return print('Operador inválido')

    # Sacar
    def sacar_saldo_corrente(self, valor):
        self.set_saldo_corrente('-', valor)

    # Depositar
    def depositar_saldo_corrente(self, valor):
        self.set_saldo_corrente('+', valor)

    # Aplicar
    def aplicar_saldo(self, valor):
        self.set_saldo_corrente('-', valor)
        self.set_saldo_poupanca('+', valor)

    # Senha do usuario:
    def senhaP(self, password):
       self.senha = password

       while True:
        senha = int(input('\nDigite uma senha de 4 digítos: \n'))


        if len(str(senha)) != 4:
            print("\n|Digite uma senha com apenas 4 digítos!|")
            continue
        else:
            print("\n|Senha cadastrada com sucesso!|")
        break
   

# Conta Pupanca
class ContaPoupanca(ContaCorrente):
    def __init__(self, nome_do_titular, numero_conta, saldo_corrente, saldo_poupanca, senha):
        super().__init__(nome_do_titular, numero_conta, saldo_corrente, saldo_poupanca, senha)


    # Resgate
    def resgatar_saldo(self, valor):
        self.set_saldo_poupanca('-', valor)
        self.set_saldo_corrente('+', valor)


#chamada

pessoa1 =