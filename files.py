import csv

DEBUG_MODE = False

def read_csv(path: str) -> list:
  data = []
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
  return data

def initialize_file(path: str) -> None:
  """Initializes a file with 10 lines, based on the provided path.

  :param path: The location path of the file to initialize.
  :type path: str
  :returns: None
  :rtype: None
  """
  things_to_write: list = []
  for i in range(1, 11):
    things_to_write.append(f"Linea {i}\n")
  with open(path, 'w+') as file:
    for line in things_to_write:
      if DEBUG_MODE:
        print(f"[log:initialize_file]___Line to append to file: {line}")
      file.write(f"{line}")


def get_length_by_file(path: str) -> int:
  """Gets the length of the file specified by the provided path.

  :param path: Location path of the file to get the length from.
  :type path: str
  :returns: length
  :rtype: int
  """
  lines: list = []
  with open(path, 'r+') as file:
    for line in file:
      lines.append(line)

  if DEBUG_MODE:
    print(f"[log:get_length_by_file]___Lines object = {lines}")

  length: int = len(lines)
  return length


def print_file(path: str) -> None:
  """Reads the whole lines of the specified file path.

  :param path: Location of the file that will be read.
  :type path: str
  :returns: None
  :rtype: NoneType
  """
  with open(path, 'r') as file:
    for each_line in file:
      print(each_line)


def write_to_file(path: str, text: str) -> None:
  """Writes a new line to a file from provided path.

  :param path: Location of the file to be written.
  :type path: str
  :param text: Text to be written to the file.
  :type text: str
  :returns: None
  :rtype: NoneType
  """
  with open(path, 'a') as file:
    file.write(f"{text}\n")
