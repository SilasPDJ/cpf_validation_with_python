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


class CPF:

    def __init__(self):
        """
        Creator: Silas B. Ferreira
        """
        # GERADOR DE CPFcurtimuitoGERADORminha-versão
        # print(self.generate())
        self.__valid_or_invalid_msg(self.generate_cpf())
        self.__valid_or_invalid_msg('44500573842')

    def generate_cpf(self):
        # já gera válido

        cpf_will_be = ''
        from random import randint
        for i in range(9):
            digt = randint(0, 9)
            cpf_will_be += str(digt)
        # ou então:
        # str(randint(123456789,987654321))
        # tanto faz os números, ele vai fazer random de qualquer jeito, muito legal...

        cpf = cpf_will_be.replace(' ', '')

        cpf_10d = self.valida_cpf(cpf)
        # print('10 dígitos...')
        cpf += str(cpf_10d)

        cpf_11d = self.valida_cpf(cpf)
        # print('11 dígitos...')
        cpf += str(cpf_11d)

        cpf_final = cpf
        return cpf_final

    def valida_cpf(self, cpf):
        cont_mult = len(cpf) + 1
        list_res = []
        for en, digit in enumerate(cpf):
            cont_mult = len(cpf)+1 - en
            # print(cont_mult)
            digit = int(digit)

            res = digit * cont_mult
            list_res.append(res)

        sum_res = sum(list_res)

        final_res = 11 - (sum_res % 11)

        if final_res > 9:
            final_res = 0
        print("final res:")
        input(final_res)
        return final_res

    # ACIMA ESTÁ UM GERADOR
    """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    # ABAIXO ESTÁ UM VALIDADOR

    def __valid_or_invalid_msg(self, cpf):
        # EXECUTA
        if self.valid_or_invalid(cpf):
            print(f'O CPF: {cpf} é VÁLIDO')
        else:
            print(f'O CPF: {cpf} NÃO é VÁLIDO')
        # valida_cpf(cpf)

    def valid_or_invalid(self, cpf):
        # valid or invalid
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
                print('-='*30)
                print(f'Os últimos dígitos devem ser: {pen}, {ult}')
                return False
            else:
                return True
        else:
            print(
                'CPFcurtimuitoGERADORminha-versão tem que ser numérico apenas e ter apenas 11 caracteres...')


CPF()
