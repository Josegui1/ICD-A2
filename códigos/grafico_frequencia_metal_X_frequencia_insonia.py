# Linechart empilhado 

#importando módulo principal

import modulo_principal as mp

def linechart_empilhado():
    # servindo os dados ao ColumnDataSource

    dataframe_never = mp.dataframe.loc[mp.dataframe["Frequency [Metal]"] == "Never"]
    dataframe_sometimes = mp.dataframe.loc[mp.dataframe["Frequency [Metal]"] == "Sometimes"]
    dataframe_rarely = mp.dataframe.loc[mp.dataframe["Frequency [Metal]"] == "Rarely"]
    dataframe_very_frequently = mp.dataframe.loc[mp.dataframe["Frequency [Metal]"] == "Very frequently"]

    frequencia_surto_insonia_never = dataframe_never["Insomnia"].value_counts()
    frequencia_surto_insonia_sometimes = dataframe_sometimes["Insomnia"].value_counts()
    frequencia_surto_insonia_rarely = dataframe_rarely["Insomnia"].value_counts()
    frequencia_surto_insonia_very_frequently = dataframe_very_frequently["Insomnia"].value_counts()

        #Criando dados ordenados para Frequency [Metal] == "Never" 

    never_data_sorted = dict(sorted(dict(frequencia_surto_insonia_never).items()))
    index_never = list(never_data_sorted.keys())
    frequencias_never = list(never_data_sorted.values())
    data_never = {"index_never": list(never_data_sorted.keys()), "frequencias_never": list(never_data_sorted.values())}
    source_never = mp.ColumnDataSource(data = data_never)

        #Criando dados ordenados para Frequency [Metal] == "Rarely" 

    rarely_data_sorted = dict(sorted(dict(frequencia_surto_insonia_rarely).items()))
    index_rarely = list(rarely_data_sorted.keys())
    frequencias_rarely = list(rarely_data_sorted.values())
    data_rarely = {"index_rarely": list(rarely_data_sorted.keys()), "frequencias_rarely": list(rarely_data_sorted.values())}
    source_rarely = mp.ColumnDataSource(data = data_rarely)
        
        #Criando dados ordenados para Frequency [Metal] == "Sometimes" 

    sometimes_data_sorted = dict(sorted(dict(frequencia_surto_insonia_sometimes).items()))
    index_sometimes = list(sometimes_data_sorted.keys())
    frequencias_sometimes = list(sometimes_data_sorted.values())
    data_sometimes = {"index_sometimes": list(sometimes_data_sorted.keys()), "frequencias_sometimes": list(sometimes_data_sorted.values())}
    source_sometimes = mp.ColumnDataSource(data = data_sometimes)
        
        #Criando dados ordenados para Frequency [Metal] == "Very frequently" 

    very_frequently_data_sorted = dict(sorted(dict(frequencia_surto_insonia_very_frequently).items()))
    index_very_frequently = list(very_frequently_data_sorted.keys())
    frequencias_very_frequently = list(very_frequently_data_sorted.values())
    data_very_frequently = {"index_very_frequently": list(very_frequently_data_sorted.keys()), "frequencias_very_frequently": list(very_frequently_data_sorted.values())}
    source_very_frequently = mp.ColumnDataSource(data = data_very_frequently)
        
    # Criando o gráfico em si

    mp.output_file("grafico_frequencia_metal_X_frequencia_insonia.html")

    linechart_empilhado = mp.figure(width = 1000)
    linechart_empilhado.line(x = "index_never", y = "frequencias_never", source = source_never, color = (196, 146, 225, 0.7), width = 2, legend_label = "Never")
    linechart_empilhado.line(x = "index_rarely", y = "frequencias_rarely", source = source_rarely, color = (165, 79, 219, 0.8), width = 2, legend_label = "Rarely")
    linechart_empilhado.line(x = "index_sometimes", y = "frequencias_sometimes", source = source_sometimes, color = (127, 61, 168, 0.8), width = 2, legend_label = "Sometimes")
    linechart_empilhado.line(x = "index_very_frequently", y = "frequencias_very_frequently", source = source_very_frequently, color = (69, 33, 92, 0.9), width = 2, legend_label = "Very frequently")

    # Personalizações gerais do gráfico
        # Título
    linechart_empilhado.title = "Linechart empilhado frequência casos de insônia X frequência indivíduos por frequência ouve metal"
    linechart_empilhado.title_location = "above"
    linechart_empilhado.title.align = "center"
    linechart_empilhado.title.text_font_size = "20px"
    linechart_empilhado.title.text_font = "Arial"
    linechart_empilhado.title.background_fill_color = "#CCCAC6"
    linechart_empilhado.title.background_fill_alpha = 0.5
    linechart_empilhado.title.border_line_color = "black"
    linechart_empilhado.title.border_line_alpha = 0.5
        # Fundo
    linechart_empilhado.background_fill_color = "#FFFDF7"
    linechart_empilhado.grid.grid_line_alpha = 0.2
        # Eixos
    linechart_empilhado.axis.axis_label_text_font = "Arial"
    linechart_empilhado.axis.axis_label_text_font_size = "20px"

    #Personalização específica do gráfico
        # Eixos
    linechart_empilhado.xaxis.axis_label = "frequência casos insônia"
    linechart_empilhado.yaxis.axis_label = "número de pessoas"
        # Legenda
    linechart_empilhado.legend.title = "Freq. Metal"
    
    return linechart_empilhado


