#importando o módulo principal
import modulo_principal as mp

#Servindo o ColumnDataSource

dataframe_never = mp.dataframe.loc[mp.dataframe["Frequency [Classical]"] == "Never"]
dataframe_sometimes = mp.dataframe.loc[mp.dataframe["Frequency [Classical]"] == "Sometimes"]
dataframe_rarely = mp.dataframe.loc[mp.dataframe["Frequency [Classical]"] == "Rarely"]
dataframe_very_frequently = mp.dataframe.loc[mp.dataframe["Frequency [Classical]"] == "Very frequently"]

frequencia_surto_depressivo_never = dataframe_never["Age"].value_counts()
frequencia_surto_depressivo_sometimes = dataframe_sometimes["Age"].value_counts()
frequencia_surto_depressivo_rarely = dataframe_rarely["Age"].value_counts()
frequencia_surto_depressivo_very_frequently = dataframe_very_frequently["Age"].value_counts()

data = {"never": frequencia_surto_depressivo_never, "sometimes": frequencia_surto_depressivo_sometimes, "rarely": frequencia_surto_depressivo_sometimes, "very frequently": frequencia_surto_depressivo_very_frequently}
source = mp.ColumnDataSource(data = data)

# O gráfico em si

mp.output_file("grafico_frequencia_classica_X_distribuicao_idade.html")

figure = mp.figure(x_range = (0, 100), width=1000)
figure.vbar(x = frequencia_surto_depressivo_never.index, top = frequencia_surto_depressivo_never, color=(100, 50, 50, 0.5))
figure.vbar(x = frequencia_surto_depressivo_rarely.index, top = frequencia_surto_depressivo_rarely, color=(50, 100, 50, 0.5))
figure.vbar(x = frequencia_surto_depressivo_sometimes.index, top = frequencia_surto_depressivo_sometimes, color=(50, 50, 100, 0.5))
figure.vbar(x = frequencia_surto_depressivo_very_frequently.index, top = frequencia_surto_depressivo_very_frequently, color=(150, 50, 50, 0.5))
mp.show(figure)