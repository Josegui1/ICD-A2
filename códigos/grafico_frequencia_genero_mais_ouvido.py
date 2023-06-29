# Importando o módulo principal

import modulo_principal as mp

# Criando o ColumnDataSource

frequencia_absoluta_genero_favorito = mp.dataframe["Fav genre"].value_counts()
lista_estilos_ordenada = ["Rock", "Pop", "Metal", "Classical", "Video game music", "EDM", "Hip hop", "R&B", "K pop", "Folk", "Country", "Rap", "Jazz", "Lofi", "Latin", "Gospel"]

data = {"estilos": lista_estilos_ordenada, "frequencia": frequencia_absoluta_genero_favorito}   
source = mp.ColumnDataSource(data = data)

# Criando o gráfico em si

mp.output_file("frequencia_X_genero_mais_ouvido.html")

figure = mp.figure(y_range = lista_estilos_ordenada)    
figure.hbar(y = "estilos", right = "frequencia", source = source, height = 0.9)
mp.show(figure)       




