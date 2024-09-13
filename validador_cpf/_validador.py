def cpf_valido(cpf: str) -> bool:
    cpf_sem_formatacao: str = _remover_formatacao_cpf(cpf)
    if not _cpf_menor_ou_maior_que_onze(cpf_sem_formatacao):
        digitos_verificadores: str = cpf_sem_formatacao[-2:]
        digitos_verificador_esperado = _calcular_digitos_verificadores(
            cpf_sem_formatacao
        )
        if digitos_verificadores == digitos_verificador_esperado:
            return True
    return False


def _calcular_digitos_verificadores(cpf: str) -> str:
    digitos_do_cpf = list(cpf)
    primeiro_digito = _calcular_digito_verificador(digitos_do_cpf)
    segundo_digito = _calcular_digito_verificador(digitos_do_cpf, segundo_digito=True)
    return f"{primeiro_digito}{segundo_digito}"


def _calcular_digito_verificador(
    digitos_do_cpf: list[str], segundo_digito: bool = False
) -> int:
    soma_digitos_para_verificacao: int = 0
    peso = 10
    if segundo_digito:
        peso = 11

    for i in range(9):
        soma_digitos_para_verificacao += int(digitos_do_cpf[i]) * (peso - i)

    resto: int = soma_digitos_para_verificacao % 11
    digito: int = 0
    if resto >= 2:
        digito = 11 - resto

    return digito


def _remover_formatacao_cpf(cpf: str) -> str:
    return cpf.replace(".", "").replace("-", "").replace("/", "")


def _cpf_menor_ou_maior_que_onze(cpf: str) -> bool:
    return 11 > len(cpf) > 11
