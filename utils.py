def filter_data_by(data: list, column: str, col_val: str) -> list:
  if column == "*" or col_val == "*":
    return data
  result = list(filter(lambda c: c[column].upper() == col_val.upper(), data))
  return result

def number_formatter(number: int or float or str) -> str:
  return '{:,}'.format(number)
