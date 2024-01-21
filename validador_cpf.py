
regioes_emissoras_cpf = {
    '1':'DF, GO, MS, MT ou TO',
    '2':'AC, AM, AP, PA, RO ou RR',
    '3':'CE, MA ou PI',
    '4':'AL, PB, PE ou RN',
    '5':'BA ou SE',
    '6':'MG',
    '7':'ES ou RJ',
    '8':'SP',
    '9':'PR ou SC',
    '0':'RS'
}

# Calcula o primeiro digito verificador do cpf
def calcula_digito1(cpf): 
    soma_digito1 = 0
    indice_digito1 = 10

    for numero in cpf[:9]:
        soma_digito1 += indice_digito1 * int(numero)
        indice_digito1 -= 1

    resto_digito1 = soma_digito1 % 11

    if resto_digito1 <= 1:
        return str(0)
    else:
        return str(11 - resto_digito1)
    
# Calcula o segundo digito verificador do cpf
def calcula_digito2(cpf):
    soma_digito2 = 0
    indice_digito2 = 11

    for numero in cpf[:10]:
        soma_digito2 += indice_digito2 * int(numero)
        indice_digito2 -= 1

    resto_digito2 = soma_digito2 % 11

    if resto_digito2 <= 1:
        return str(0)
    else:
        return str(11 - resto_digito2)

# Utilizando as funções de calcular os digitos verificadores, compara com que foi informado no cpf do usuário
def valida_cpf(cpf):
    if cpf[9] == calcula_digito1(cpf) and cpf[10] == calcula_digito2(cpf):
        return True
    else:
        return False

while True:
    cpf_informado = input('informe o seu CPF: ').replace('.', '').replace('-', '').replace(' ', '')
    if len(cpf_informado) !=  11:
        print('Formato do CPF é inválido, digite novamente.')
        print()
    else:
        break
# Imprime na tela o status do cpf informado
if valida_cpf(cpf_informado):
    print(f'O CPF é valido, a região de emissão é {regioes_emissoras_cpf[cpf_informado[8]]}')
else:
    print('O CPF é inválido.')