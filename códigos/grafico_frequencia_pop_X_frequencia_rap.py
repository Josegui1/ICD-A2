# Heatmap por transpar√™ncia

# importando m√≥dulo principal

import modulo_principal as mp

def heatmap_transparencia():
    # servindo os dados ao ColumnsDataSource

    frequencia_eixo_x = ["Never", "Rarely", "Sometimes", "Very frequently",
                         "Never", "Rarely", "Sometimes", "Very frequently",
                         "Never", "Rarely", "Sometimes", "Very frequently",
                         "Never", "Rarely", "Sometimes", "Very frequently"]
    frequencia_eixo_y = ["Never", "Never", "Never", "Never",
                         "Rarely", "Rarely", "Rarely", "Rarely",
                         "Sometimes", "Sometimes", "Sometimes", "Sometimes",
                         "Very frequently", "Very frequently", "Very frequently", "Very frequently"]

    gradiente = [0.330, 0.510, 0.630, 0.570,
                 0.090, 0.390, 0.930, 0.750,
                 0.150, 0.270, 0.690, 0.870,
                 0.030, 0.210, 0.450, 0.810]

    valores_numericos_ordenados = ["27", "41", "49", "42",
                                   "8", "34", "80", "58",
                                   "10", "25", "52", "79",
                                   "2", "16", "35", "63"]

    data = {"frequencia_eixo_x": frequencia_eixo_x, 
            "frequencia_eixo_y": frequencia_eixo_y,
            "gradiente": gradiente,
            "valores_numericos_ordenados": valores_numericos_ordenados}
    source = mp.ColumnDataSource(data = data)

    #O gr√°fico em si

    mp.output_file("grafico_frequencia_rap_X_frequencia_pop.html")

    heatmap_transparencia = mp.figure(x_range = ["Never", "Rarely", "Sometimes", "Very frequently"],
                       y_range = ["Never", "Rarely", "Sometimes", "Very frequently"], width = 1000)
    heatmap_transparencia.rect(x = "frequencia_eixo_x", y = "frequencia_eixo_y", color = "darkred", fill_alpha = "gradiente", width = 1, height = 1, source = source)
    numeros = mp.LabelSet(x = "frequencia_eixo_x", y = "frequencia_eixo_y", text = "valores_numericos_ordenados", source = source, render_mode = "canvas")
    heatmap_transparencia.add_layout(numeros) # Utilizei isto para plotar os n√∫meros respectivos de cada par do heatmap

    # Personaliza√ß√µes gerais do gr√°fico
        # T√≠tulo
    heatmap_transparencia.title = "Heatmap feito com transparÍncia frequÍncia ouve pop X frequÍncia ouve rap"
    heatmap_transparencia.title_location = "above"
    heatmap_transparencia.title.align = "center"
    heatmap_transparencia.title.text_font_size = "20px"
    heatmap_transparencia.title.text_font = "Arial"
    heatmap_transparencia.title.background_fill_color = "#CCCAC6"
    heatmap_transparencia.title.background_fill_alpha = 0.5
    heatmap_transparencia.title.border_line_color = "black"
    heatmap_transparencia.title.border_line_alpha = 0.5
        # Fundo
    heatmap_transparencia.background_fill_color = "#FFFDF7"
    heatmap_transparencia.grid.grid_line_alpha = 0.2
        # Eixos
    heatmap_transparencia.axis.axis_label_text_font = "Arial"
    heatmap_transparencia.axis.axis_label_text_font_size = "20px"

    # Personaliza√ß√£o espec√≠fica do gr√°fico
        # Eixos
    heatmap_transparencia.xaxis.axis_label = "frequÍncia pop"
    heatmap_transparencia.yaxis.axis_label = "frequÍncia rap"
    
    return heatmap_transparencia

   # Este gr·fico tambÈm n„o pode ser posto no servidor bokeh
   

