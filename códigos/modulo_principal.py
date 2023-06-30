# Importando as bibliotecas necessárias
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, LabelSet

# Criando o dataframe

dataframe = pd.read_csv(r"C:\Users\jguil\Documents\Datasets_for_analysis\Music_and_mental_health_dataset\mxmh_survey_results.csv")

# Limpando algumas coisas no dataframe

dataframe = dataframe.loc[dataframe["BPM"] <= 500] 
dataframe = dataframe.loc[dataframe["BPM"] >= 30] 
dataframe = dataframe.loc[dataframe["Hours per day"] <= 24]

