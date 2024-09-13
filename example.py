from main import cpf_valido

cpf = input("Digite o cpf a ser verificado: ")

resultado: bool = cpf_valido(cpf)
print(resultado)
