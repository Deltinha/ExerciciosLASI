import pandas as pd

unidadesConsumidoras = pd.read_excel('data_uc.xlsx')
dadosCorporacao = pd.read_excel("data_ts.xlsx")

linhasUC = unidadesConsumidoras.shape[0]
linhasBanco = dadosCorporacao.shape[0]

unidadesNaoPresentes = []

for i in range(0,linhasUC):
    unidadePresente = False
    for j in range(0,linhasBanco):
        if unidadesConsumidoras['UC_TOT'][i] == dadosCorporacao['UC'][j]:
            unidadePresente = True
    
    if unidadePresente == False:
        unidadesNaoPresentes.append(unidadesConsumidoras['UC_TOT'][i])
     
print(f'As unidades consumidoras não presentes no banco de dados da corporação são:\n{unidadesNaoPresentes}')
