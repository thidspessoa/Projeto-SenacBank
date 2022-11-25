#Inputs




#Função
class revirarSenha 
def senha_bank (self, password):
    self.senha = password
    
    return password
    



#chamada

print("\n+----------   Bem vindo ao senac Bank       ----------+")
print("|  Primeiro vamos criar sua senha de acesso ao banco  |")

senha = int(input("\nDigite sua senha de acesso, de 4 digitos: "))

func1 = senha_bank()
senha_bank(senha)
#print(senha_bank.senha)

