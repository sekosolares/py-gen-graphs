from utils import filter_data_by
from files import read_csv
from charts import generate_barchart, generate_piechart
import pandas as pd

if __name__ == '__main__':
  csv_data = read_csv('./data.csv')
  filter_column = input("Filter by column => ")
  filter_value = input("Type a filter value => ")
  select_columns = input(
    "Which column(s) to select (comma separated if many)? => "
  )

  print("Type the number of the chart you want to generate:")
  print("1. bar")
  print("2. pie")
  chart = int(input(" => "))

  select_columns = select_columns.split(',')
  datalist_country = filter_data_by(csv_data, filter_column, filter_value)

  if len(datalist_country) == 1:
    data = datalist_country[0]
    labels = select_columns
    values = [data[val] for val in labels]
    labels = [
      txt[:4] if 'population' in txt.lower() else txt for txt in labels
    ]
    values = [int(val) if int(val) else val for val in values]
  else:
    labels = select_columns
    country_datalist = [country_data for country_data in datalist_country]
    values = [[country[val] for val in labels] for country in country_datalist]

  if chart == 1:
    print("Bar Chart...")
    generate_barchart(labels, values)
  elif chart == 2:
    labels = select_columns[:2]
    country_datalist = [country_data for country_data in datalist_country]
    values = [[country[val] for val in labels] for country in country_datalist]
    labels = [data[0] for data in values]
    values = [data[1] for data in values]
    print("Pie Chart...")
    generate_piechart(labels, values)
  else:
    print("Invalid chart number!")
    exit(1)
