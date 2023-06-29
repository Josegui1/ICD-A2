# importando o modulo principal

import modulo_principal as mp

# Servindo de dados o ColumnDataSource 

dataframe_never = mp.dataframe.loc[mp.dataframe["Frequency [Rap]"] == "Never"]
dataframe_sometimes = mp.dataframe.loc[mp.dataframe["Frequency [Rap]"] == "Sometimes"]
dataframe_rarely = mp.dataframe.loc[mp.dataframe["Frequency [Rap]"] == "Rarely"]
dataframe_very_frequently = mp.dataframe.loc[mp.dataframe["Frequency [Rap]"] == "Very frequently"]

frequencia_surto_depressivo_never = dataframe_never["Depression"].value_counts()
frequencia_surto_depressivo_sometimes = dataframe_sometimes["Depression"].value_counts()
frequencia_surto_depressivo_rarely = dataframe_rarely["Depression"].value_counts()
frequencia_surto_depressivo_very_frequently = dataframe_very_frequently["Depression"].value_counts()

data = {"never": frequencia_surto_depressivo_never, "sometimes": frequencia_surto_depressivo_sometimes, "rarely": frequencia_surto_depressivo_sometimes, "very frequently": frequencia_surto_depressivo_very_frequently}
source = mp.ColumnDataSource(data = data)
# Criando o gráfico em si

mp.output_file("grafico_frequencia_ouve_rap_X_frequencia_surtos_depressivos.html")

figure = mp.figure()

figure.circle(x = frequencia_surto_depressivo_never, y = frequencia_surto_depressivo_never.index, color="red")
figure.circle(x = frequencia_surto_depressivo_rarely, y = frequencia_surto_depressivo_rarely.index, color="blue")
figure.circle(x = frequencia_surto_depressivo_sometimes, y = frequencia_surto_depressivo_sometimes.index, color="green")
figure.circle(x = frequencia_surto_depressivo_very_frequently, y = frequencia_surto_depressivo_very_frequently.index, color="purple")

mp.show(figure)




"""
Never
Sometimes
Rarely
Very frequently
"""