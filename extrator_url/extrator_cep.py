import re

endereco = "Rua Itu 86, apartamento 144, Cambuí, Campinas, SP, 13025340"

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)

cpf = "374.672.318-30"

padrad_cpf = re.compile("([0-9]{3}[.]?){2}([0-9]{3}[-]?)([0-9]{2})")

Luis = "Luis Eduardo Angelini Marquitti, CPF: 374.672.318-30"

busca_cpf = padrad_cpf.search(Luis)

if busca_cpf:
    cpf = busca_cpf.group()
    print(cpf)
