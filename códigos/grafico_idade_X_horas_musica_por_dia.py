# Scatterplot simples

#Importando o módulo principal

import modulo_principal as mp

def scatterplot_simples():
    #Criando o ColumnDataSource referente ao gráfico proposto

    data = {"idade" : mp.dataframe["Age"], "horas por dia" : mp.dataframe["Hours per day"]}
    source = mp.ColumnDataSource(data = data)

    #Criando o gráfico em si

    mp.output_file("Idade_X_Horas_por_dia.html")

    scatterplot_simples = mp.figure(width = 1000)
    scatterplot_simples.triangle(x = "idade", y = "horas por dia", color = "black", source = source)

    # Personalizações gerais do gráfico
        # Título
    scatterplot_simples.title = "Scatterplot simples idade X horas de música por dia"
    scatterplot_simples.title_location = "above"
    scatterplot_simples.title.align = "center"
    scatterplot_simples.title.text_font_size = "20px"
    scatterplot_simples.title.text_font = "Arial"
    scatterplot_simples.title.background_fill_color = "#CCCAC6"
    scatterplot_simples.title.background_fill_alpha = 0.5
    scatterplot_simples.title.border_line_color = "black"
    scatterplot_simples.title.border_line_alpha = 0.5
        # Fundo
    scatterplot_simples.background_fill_color = "#FFFDF7"
    scatterplot_simples.grid.grid_line_alpha = 0.2
        # Eixos
    scatterplot_simples.axis.axis_label_text_font = "Arial"
    scatterplot_simples.axis.axis_label_text_font_size = "20px"

    # Personalização específica
    scatterplot_simples.xaxis.axis_label = "idade"
    scatterplot_simples.yaxis.axis_label = "horas de música por dia"
    
    return scatterplot_simples



