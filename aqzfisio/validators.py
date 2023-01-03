import re


def cpf_valido(numero_do_cpf):
    return (numero_do_cpf) == 11


def nome_valido(nome):
    return nome.isalpha()


def celular_valido(numero_celular):
    """Verifica se o celular é valido (85 87451-1254)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta

