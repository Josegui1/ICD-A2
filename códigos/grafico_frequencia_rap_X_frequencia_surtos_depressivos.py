# Scatterplot múltiplo

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

    # Dados never
data_never = {"never": frequencia_surto_depressivo_never, "indice": frequencia_surto_depressivo_never.index}
source_never = mp.ColumnDataSource(data = data_never)
    # Dados rarely
data_rarely = {"rarely": frequencia_surto_depressivo_rarely, "indice": frequencia_surto_depressivo_rarely.index}
source_rarely = mp.ColumnDataSource(data = data_rarely)
    # Dados sometimes
data_sometimes = {"sometimes": frequencia_surto_depressivo_sometimes, "indice": frequencia_surto_depressivo_sometimes.index}
source_sometimes = mp.ColumnDataSource(data = data_sometimes)
    # Dados very frequently
data_very_frequently = {"very frequently": frequencia_surto_depressivo_very_frequently, "indice": frequencia_surto_depressivo_very_frequently.index}
source_very_frequently = mp.ColumnDataSource(data = data_very_frequently)


# Criando o gráfico em si

mp.output_file("grafico_frequencia_ouve_rap_X_frequencia_surtos_depressivos.html")

scatterplot_multiplo = mp.figure(width = 1000)

scatterplot_multiplo.circle(x = "never", y = "indice", source = source_never, color="#EEB9B0", size = 7, legend_label = "Never")
scatterplot_multiplo.circle(x = "rarely", y = "indice", source = source_rarely ,color="#E15344", size = 7, legend_label = "Rarely")
scatterplot_multiplo.circle(x = "sometimes", y = "indice", source = source_sometimes , color="#B01500", size = 7, legend_label = "Sometimes")
scatterplot_multiplo.circle(x = "very frequently", y = "indice", source = source_very_frequently, color="#000000", size = 7, legend_label = "Very frequently")

# Personalizações gerais do gráfico
    # Título
scatterplot_multiplo.title = "Scatterplot múltiplo frequência indivíduos X  frequência casos depressivos por frequência ouve rap"
scatterplot_multiplo.title_location = "above"
scatterplot_multiplo.title.align = "center"
scatterplot_multiplo.title.text_font_size = "20px"
scatterplot_multiplo.title.text_font = "Arial"
scatterplot_multiplo.title.background_fill_color = "#CCCAC6"
scatterplot_multiplo.title.background_fill_alpha = 0.5
scatterplot_multiplo.title.border_line_color = "black"
scatterplot_multiplo.title.border_line_alpha = 0.5
    # Fundo
scatterplot_multiplo.background_fill_color = "#FFFDF7"
scatterplot_multiplo.grid.grid_line_alpha = 0.2
    # Eixos
scatterplot_multiplo.axis.axis_label_text_font = "Arial"
scatterplot_multiplo.axis.axis_label_text_font_size = "20px"

#Personalização específica do gráfico
    # Eixo
scatterplot_multiplo.xaxis.axis_label = "número de pessoas"
scatterplot_multiplo.yaxis.axis_label = "frequência casos depressão"
    # Legenda
scatterplot_multiplo.legend.title = "Freq. Rap"

# Exibindo o gráfico

mp.show(scatterplot_multiplo)

