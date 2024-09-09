def descobre_numero_verificador(lista_numeros, lista_numeros_cpf):
    soma_num_ver = 0
    for i in range(len(lista_numeros)):
        soma_num_ver += int(lista_numeros_cpf[i]) * int(lista_numeros[i])

    resto = soma_num_ver % 11
    num_verificador = 0
    if resto >= 2:
        num_verificador = 11 - resto

    return num_verificador


cpf = input("Digite o cpf a ser verificado: ")
cpf.replace(".", "")
cpf.replace("-", "")
cpf.replace("/", "")

if len(cpf) != 11:
    print(
        "Cpf tem menos/mais de 11 caracteres verifique se o cpf informado está correto"
    )
    exit()

lista_de_numero_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
lista_de_numero_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3]

numeros_do_cpf = list(cpf)

verificador_1 = descobre_numero_verificador(lista_de_numero_1, numeros_do_cpf)
verificador_2 = descobre_numero_verificador(lista_de_numero_2, numeros_do_cpf)

numero_verificador_1 = int(numeros_do_cpf[9])
numero_verificador_2 = int(numeros_do_cpf[10])

if numero_verificador_1 != verificador_1 or numero_verificador_2 != verificador_2:
    print("O Cpf informado não é um cpf valido!")
    exit()

print("Cpf informado é valido")
