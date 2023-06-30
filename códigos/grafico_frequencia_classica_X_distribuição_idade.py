# Histograma empilhado

#importando o módulo principal
import modulo_principal as mp

#Servindo o ColumnDataSource

dataframe_never = mp.dataframe.loc[mp.dataframe["Frequency [Classical]"] == "Never"]
dataframe_sometimes = mp.dataframe.loc[mp.dataframe["Frequency [Classical]"] == "Sometimes"]
dataframe_rarely = mp.dataframe.loc[mp.dataframe["Frequency [Classical]"] == "Rarely"]
dataframe_very_frequently = mp.dataframe.loc[mp.dataframe["Frequency [Classical]"] == "Very frequently"]

frequencia_idade_never = dataframe_never["Age"].value_counts()
frequencia_idade_sometimes = dataframe_sometimes["Age"].value_counts()
frequencia_idade_rarely = dataframe_rarely["Age"].value_counts()
frequencia_idade_very_frequently = dataframe_very_frequently["Age"].value_counts()

    # Dados never
data_never = {"never": frequencia_idade_never, "frequencia": frequencia_idade_never.index}
source_never = mp.ColumnDataSource(data = data_never)

    # Dados rarely
data_rarely = {"rarely": frequencia_idade_rarely, "frequencia": frequencia_idade_rarely.index}
source_rarely = mp.ColumnDataSource(data = data_rarely)

    # Dados sometimes
data_sometimes = {"sometimes": frequencia_idade_sometimes, "frequencia": frequencia_idade_sometimes.index}
source_sometimes = mp.ColumnDataSource(data = data_sometimes)

    # Dados very frequently
data_very_frequently = {"very frequently": frequencia_idade_very_frequently, "frequencia": frequencia_idade_very_frequently.index}
source_very_frequently = mp.ColumnDataSource(data = data_very_frequently)

# O gráfico em si

mp.output_file("grafico_frequencia_classica_X_distribuicao_idade.html")

histograma_empilhado = mp.figure(x_range = (0, 100), width=1000)

histograma_empilhado.vbar(x = "frequencia", top = "never", source = source_never, color=(238, 116, 71, 0.3), legend_label = "Never")
histograma_empilhado.vbar(x = "frequencia", top = "rarely", source = source_rarely, color=(235, 70, 0, 0.5), legend_label = "Rarely")
histograma_empilhado.vbar(x = "frequencia", top = "sometimes", source = source_sometimes, color=(171, 50, 0, 0.6), legend_label = "Sometimes")
histograma_empilhado.vbar(x = "frequencia", top = "very frequently", source = source_very_frequently, color=(100, 32, 0, 0.8), legend_label = "Very frequently")

# Personalizações gerais do gráfico
    # Título
histograma_empilhado.title = "Histogramas distribuição de idade X frequencia ouve música clássica"
histograma_empilhado.title_location = "above"
histograma_empilhado.title.align = "center"
histograma_empilhado.title.text_font_size = "20px"
histograma_empilhado.title.text_font = "Arial"
histograma_empilhado.title.background_fill_color = "#CCCAC6"
histograma_empilhado.title.background_fill_alpha = 0.5
histograma_empilhado.title.border_line_color = "black"
histograma_empilhado.title.border_line_alpha = 0.5
    # Fundo
histograma_empilhado.background_fill_color = "#FFFDF7"
histograma_empilhado.grid.grid_line_alpha = 0.2
    # Eixos
histograma_empilhado.axis.axis_label_text_font = "Arial"
histograma_empilhado.axis.axis_label_text_font_size = "20px"

# Personalização específica do gráfico
    # Eixo
histograma_empilhado.xaxis.axis_label = "idade"
histograma_empilhado.yaxis.axis_label = "frequência de pessoas"
    # Legenda
histograma_empilhado.legend.title = "Freq. Class."


# Exibindo o gráfico

mp.show(histograma_empilhado)