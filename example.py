import validador_cpf as vc

cpf = input("Digite o cpf a ser verificado: ")

resultado: bool = vc.cpf_valido(cpf)
print(resultado)
