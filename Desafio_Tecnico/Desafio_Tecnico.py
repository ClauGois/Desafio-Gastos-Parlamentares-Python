import pandas as pd
import warnings
warnings.filterwarnings("ignore")

class perguntas:
    def pergunta1(self):
        print('1 - Qual estado e partido têm a maior soma do valor líquido nos anos de 2009 e 2020?')
        print('\n')
    def pergunta2(self):
        print('2 - Qual é o maior número da carteira parlamentar em SC ?')
        print('\n')
    def pergunta3(self):
        print('3 - Entre 01/01/2019 e 30/06/2020, nos estados de SP, RJ e SC, qual a quantidade de registros em cada estado para o período indicado?')
        print('\n')
    def pergunta4(self):
        print('4 - Considerando o ano de 2019, quais foram os 5 partidos que mais gastaram (valor líquido) '
        'com serviço de táxi e que tiveram pelo menos uma restituição nesse período? (Apresentar'
        'ambos os valores limitados a duas casas decimais)')
        print('\n')
    def pergunta5(self):
        print('5 - Considerando o ano de emissão como sendo 2019 e 2020, exiba as 3 siglas partidárias que'
        'mais gastaram cota parlamentar (valores líquidos) para trechos que contenham "POA" ou "FLN".')
        print('\n')

class respostas:
    def __init__(self):
        self.data = pd.read_csv('cota-parlamentar.csv')
        self.partidos = self.data['sgpartido'].unique()
        self.estados = self.data['sguf'].unique()
        
    def resposta_pergunta1Partido(self,ano):
        maiorValorGasto = 0
        partidoMaiorGasto = []
        for partido in self.partidos:
            valor = self.data['vlrliquido'].loc[(self.data['sgpartido']==partido) & (self.data['numano']==ano)].sum().round(2)
            if valor > maiorValorGasto:
                maiorValorGasto = valor
                partidoMaiorGasto = partido
        print('O partido com maior gasto no ano de',ano,'foi o',partidoMaiorGasto,'com R$:', maiorValorGasto)
    
    def resposta_pergunta1Estado(self,ano):
        maiorValorGasto = 0
        estadoMaiorGasto = []
        for estado in self.estados:
            valor = self.data['vlrliquido'].loc[(self.data['sguf']==estado) & (self.data['numano']==ano)].sum().round(2)
            if valor > maiorValorGasto:
                maiorValorGasto = valor
                estadoMaiorGasto = estado
        print('O Estado com maior gasto no ano de',ano,'foi',estadoMaiorGasto,'com R$:', maiorValorGasto)


    def resposta_pergunta2(self,estado):
        maior = int(self.data['nucarteiraparlamentar'].loc[self.data['sguf']==estado].max())
        print('O maior nÚmero de carteira do estado de',estado,'é de',maior)
        
    def resposta_pergunta3(self,dataInicio,dataFim,estado):
        data3 = self.data.dropna(subset=['datemissao'])
        data3['datemissao'] = pd.to_datetime(data3['datemissao'],errors = 'coerce')
        data3.dropna(subset=['datemissao'], inplace=True)  
        registros = len(data3.loc[(data3['datemissao']>=dataInicio) & (data3['datemissao']<=dataFim ) & (data3['sguf']==estado)])
        print('O estado de',estado,'obteve',registros,'registros de',dataInicio,' a ',dataFim)
        
    def resposta_pergunta4(self,servico,ano):
        data4 = self.data.loc[(self.data['txtdescricao'] == servico) & (self.data['numano']==ano)]
        partidos = data4['sgpartido'].loc[(data4['vlrrestituicao'].notnull()) & (data4['vlrrestituicao'] > 0 )].unique()
        df = pd.DataFrame()
        for partido in partidos:
            valor=data4['vlrliquido'].loc[data4['sgpartido']==partido].sum().round(2)
            df = df.append({'Partido': partido, 'ValorLiquido': valor},ignore_index=True)
            
        print('Os 5 partidos que mais gastaram com',servico,'no ano de',ano,'e receberam restituição:')
        print(pd.DataFrame(df).sort_values('ValorLiquido',ascending=False).head(5))
        
    def resposta_pergunta5(self,trecho1,trecho2,ano1,ano2):
        data5 = self.data[['numano', 'txttrecho','sgpartido','vlrliquido']].loc[(self.data['numano']==ano1) | (self.data['numano']==ano2)]
        data5.dropna(subset=['txttrecho'],inplace=True)
        data5 = data5[data5['txttrecho'].str.contains((trecho1),(trecho2))]
        print('Os 3 partidos que mais gastaram cota parlamentamentar com os trechos',trecho1,'e',trecho2,':')
        print(data5.sort_values('vlrliquido', ascending=False).head(3))

def main():
    rps = respostas()
    pts = perguntas()

    pts.pergunta1()
    rps.resposta_pergunta1Estado(2009)
    rps.resposta_pergunta1Partido(2009)
    rps.resposta_pergunta1Estado(2020)
    rps.resposta_pergunta1Partido(2020)
    
    pts.pergunta2()
    rps.resposta_pergunta2('SC')

    pts.pergunta3()
    dataIni = '2019-01-01'
    dataFim = '2020-06-30'
    rps.resposta_pergunta3(dataIni,dataFim, 'SC')
    rps.resposta_pergunta3(dataIni,dataFim, 'SP')
    rps.resposta_pergunta3(dataIni,dataFim, 'RJ')

    servico = 'SERVIÇO DE TÁXI, PEDÁGIO E ESTACIONAMENTO'
    pts.pergunta4()
    rps.resposta_pergunta4(servico,2019)

    pts.pergunta5()
    rps.resposta_pergunta5('POA','FLN',2019,2020)
if __name__ == '__main__':
    main()
