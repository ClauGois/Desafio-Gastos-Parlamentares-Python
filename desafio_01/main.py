from perguntas import perguntas
from respostas import respostas

def main():
    rps = respostas()
    pts = perguntas()

    pts.pergunta1()
    rps.pergunta1Estado(2009)
    rps.pergunta1Partido(2009)
    rps.pergunta1Estado(2020)
    rps.pergunta1Partido(2020)
    pts.pergunta2()
    rps.pergunta2('SC')

    pts.pergunta3()
    dataIni = '2019-01-01'
    dataFim = '2020-06-30'
    rps.pergunta3(dataIni,dataFim, 'SC')
    rps.pergunta3(dataIni,dataFim, 'SP')
    rps.pergunta3(dataIni,dataFim, 'RJ')

    servico = 'SERVIÇO DE TÁXI, PEDÁGIO E ESTACIONAMENTO'
    pts.pergunta4()
    rps.pergunta4(servico,2019)

    pts.pergunta5()
    rps.pergunta5('POA','FLN',2019,2020)
if __name__ == '__main__':
    main()
