def aumentar(preço=0, taxa=0, formato=False):
    '''
    FUnção que aumenta em taxa um valor.
    :param preço: valor.
    :param taxa: valor em % a ser aumentado.
    :param formato: se vai ser formatado com R$ e virgulas.
    :return: retorna o resultado.
    '''
    res = preço + ((preço*taxa) /100 )
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    '''
    Função que diminue em taxa um valor.
    :param preço: valor.
    :param taxa: valor em % a ser aumentado.
    :param formato: se vai ser formatado com R$ e virgulas.
    :return: retorna o resultado.
    '''
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    '''
    DObra o valor.
    :param preço: valor.
    :param formato: se vai ser formatado com R$ e virgulas.
    :return: retorna o valor.
    '''
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    '''
    Divide em dois o valor.
    :param preço: valor.
    :param formato: se vai ser formatado com R$ e virgulas.
    :return: retorna o valor.
    '''
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda="R$"):
    '''
    formata um valor solicitado.
    :param preço: valor.
    :param moeda: formatação do valor.
    :return: valor formatado.
    '''
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    '''
    Resume uma string mostrando no console como seria o valor.
    :param preço: o valor.
    :param taxaa: o valor taxa somados.
    :param taxar: o valor taxa subtraidos.
    :return: sem retorno.
    '''
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analizado: \t{moeda(preço)}')
    print(f'Dobro do preço:  \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de diminuição: \t{diminuir(preço,taxar, True)}')
    print('-'*30)

