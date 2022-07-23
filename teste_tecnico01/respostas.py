import pandas as pd
import warnings
warnings.filterwarnings("ignore")
class respostas:
    def __init__(self):
        self.data = pd.read_csv('cota-parlamentar.csv')
        self.partidos = self.data['sgpartido'].unique()
        self.estados = self.data['sguf'].unique()
        
    def pergunta1Partido(self,ano):
        maiorValorGasto = 0
        partidoMaiorGasto = []
        for partido in self.partidos:
            valor = self.data['vlrliquido'].loc[(self.data['sgpartido']==partido) & (self.data['numano']==ano)].sum().round(2)
            if valor > maiorValorGasto:
                maiorValorGasto = valor
                partidoMaiorGasto = partido
        print('O partido com maior gasto no ano de',ano,'foi o',partidoMaiorGasto,'com R$:', maiorValorGasto)
    
    def pergunta1Estado(self,ano):
        maiorValorGasto = 0
        estadoMaiorGasto = []
        for estado in self.estados:
            valor = self.data['vlrliquido'].loc[(self.data['sguf']==estado) & (self.data['numano']==ano)].sum().round(2)
            if valor > maiorValorGasto:
                maiorValorGasto = valor
                estadoMaiorGasto = estado
        print('O Estado com maior gasto no ano de',ano,'foi',estadoMaiorGasto,'com R$:', maiorValorGasto)


    def pergunta2(self,estado):
        maior = int(self.data['nucarteiraparlamentar'].loc[self.data['sguf']==estado].max())
        print('O maior nÚmero de carteira do estado de',estado,'é de',maior)
        
    def pergunta3(self,dataInicio,dataFim,estado):
        data3 = self.data.dropna(subset=['datemissao'])
        data3['datemissao'] = pd.to_datetime(data3['datemissao'],errors = 'coerce')
        data3.dropna(subset=['datemissao'], inplace=True)  
        registros = len(data3.loc[(data3['datemissao']>=dataInicio) & (data3['datemissao']<=dataFim ) & (data3['sguf']==estado)])
        print('O estado de',estado,'obteve',registros,'registros de',dataInicio,' a ',dataFim)
        
    def pergunta4(self,servico,ano):
        data4 = self.data.loc[(self.data['txtdescricao'] == servico) & (self.data['numano']==ano)]
        partidos = data4['sgpartido'].loc[(data4['vlrrestituicao'].notnull()) & (data4['vlrrestituicao'] > 0 )].unique()
        df = pd.DataFrame()
        for partido in partidos:
            valor=data4['vlrliquido'].loc[data4['sgpartido']==partido].sum().round(2)
            df = df.append({'Partido': partido, 'ValorLiquido': valor},ignore_index=True)
            
        print('Os 5 partidos que mais gastaram com',servico,'no ano de',ano,'e receberam restituição:')
        print(pd.DataFrame(df).sort_values('ValorLiquido',ascending=False).head(5))
        
    def pergunta5(self,trecho1,trecho2,ano1,ano2):
        data5 = self.data[['numano', 'txttrecho','sgpartido','vlrliquido']].loc[(self.data['numano']==ano1) | (self.data['numano']==ano2)]
        data5.dropna(subset=['txttrecho'],inplace=True)
        data5 = data5[data5['txttrecho'].str.contains((trecho1),(trecho2))]
        print('Os 3 partidos que mais gastaram cota parlamentamentar com os trechos',trecho1,'e',trecho2,':')
        print(data5.sort_values('vlrliquido', ascending=False).head(3))
    