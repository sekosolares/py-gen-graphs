from charts import generate_piechart
import pandas as pd

if __name__ == '__main__':
  df = pd.read_csv('./data.csv')

  filter_str = str(input("Type conditions for filtering (e.g. `Column` == 'Value') => "))
  label_set_column = input("Type the column from which labels will be taken from => ")
  value_set_column = input("Type the column from which values will be taken from => ")
  chart_name = input("Type the chart file name => ")

  if filter_str != "all" and filter_str != "*":
    df = df.query(filter_str)
  countries = df[label_set_column].values
  percentages = df[value_set_column].values

  generate_piechart(countries, percentages, file_name=chart_name)
