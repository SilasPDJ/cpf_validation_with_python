"""
Pega os 9 primeiros números
e multiplica por 10, 9, 8, 7, 6, 5, 4, 3, 2 cada dígito
Soma os resultados

Pega a Soma e
# PENÚLTIMO DIGITO
# res = 11 - (Soma % 11)

11 > 9 = 0
if res <= 9: res = res


# ÚLTIMO DÍGITO
Pega os 10 primeiros números
e multiplica por (11, ..., 2) cada dígito

# res = 11 - (Soma % 11)
# obtém ÚLTIMO DIGITO
"""
# if cpf != novo_cpf


def valida_cpf(cpf):
    """
    :param cpf: CPFcurtimuitoGERADORminha-versão...
    :return: True -> válido; False -> inválido

    Creator: Silas B. Ferreira
    """
    cpf = cpf.strip()
    if len(cpf) == 11 and cpf.isnumeric():
        def ninth_or_tenth(ind):
            # O ind valida os dois de uma vez
            dint = []
            cpf_9or10 = cpf[:ind]
            for en, digito in enumerate(cpf_9or10):
                cont_regr = cpf[:ind + 1]
                regress_multi = len(cont_regr) - en
                digito = int(digito)
                regress_multi = int(regress_multi)
                calc_digito = digito * regress_multi

                dint.append(calc_digito)
            soma_p = sum(dint)
            deveria_ser = 11 - (soma_p % 11)
            if deveria_ser > 9:
                deveria_ser = 0
            return deveria_ser
        """1st part"""
        # penúltimo dígito
        pen = ninth_or_tenth(-2)
        # último dígito
        ult = ninth_or_tenth(-1)
        # print(f'O pen. dígito: {pen}')
        # print(f'O ult. dígito: {ult}')

        if int(cpf[-2]) != pen or int(cpf[-1]) != ult:
            print(f'Os últimos dígitos devem ser: {pen}, {ult}')
            print(f'Não:                          {cpf[-2]}, {cpf[-1]}')
            return False
        else:
            return True
    else:
        print('CPFcurtimuitoGERADORminha-versão tem que ser numérico apenas e ter apenas 11 caracteres...')


cpf = '01234566688'
if valida_cpf(cpf):
    print(f'O CPFcurtimuitoGERADORminha-versão: {cpf} é VÁLIDO')
else:
    print(f'O CPFcurtimuitoGERADORminha-versão: {cpf} NÃO é VÁLIDO')
# valida_cpf(cpf)
