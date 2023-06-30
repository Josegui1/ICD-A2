# Gráfico de barras horizontal

# Importando o módulo principal

import modulo_principal as mp

# Criando o ColumnDataSource

frequencia_absoluta_genero_favorito = mp.dataframe["Fav genre"].value_counts()
lista_estilos_ordenada = ["Rock", "Pop", "Metal", "Classical", "Video game music", "EDM", "Hip hop", "R&B", "K pop", "Folk", "Country", "Rap", "Jazz", "Lofi", "Latin", "Gospel"]

data = {"estilos": lista_estilos_ordenada, "frequencia": frequencia_absoluta_genero_favorito}   
source = mp.ColumnDataSource(data = data)

# Criando o gráfico em si

mp.output_file("frequencia_X_genero_mais_ouvido.html")

barras_horizontais = mp.figure(y_range = lista_estilos_ordenada, width = 1000)    
barras_horizontais.hbar(y = "estilos", right = "frequencia", source = source, height = 0.9)

# Personalizações gerais do gráfico
    # Título
barras_horizontais.title = "Gráfico de barras horizontal frequência de estilos favoritos"
barras_horizontais.title_location = "above"
barras_horizontais.title.align = "center"
barras_horizontais.title.text_font_size = "20px"
barras_horizontais.title.text_font = "Arial"
barras_horizontais.title.background_fill_color = "#CCCAC6"
barras_horizontais.title.background_fill_alpha = 0.5
barras_horizontais.title.border_line_color = "black"
barras_horizontais.title.border_line_alpha = 0.5
    # Fundo
barras_horizontais.background_fill_color = "#FFFDF7"
barras_horizontais.grid.grid_line_alpha = 0.2
    # Eixos
barras_horizontais.axis.axis_label_text_font = "Arial"
barras_horizontais.axis.axis_label_text_font_size = "20px"

# Personalização específica

barras_horizontais.xaxis.axis_label= "frequência"
barras_horizontais.yaxis.axis_label = "estilos favoritos"

# Exibindo o gráfico

mp.show(barras_horizontais)       




