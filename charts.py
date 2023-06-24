import matplotlib.pyplot as plt
import random

def generate_barchart(labels: list, values: list):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  rand = random.randrange(1, 100)
  plt.savefig('./charts/chart_%s.png' % rand)
  plt.close()

def generate_piechart(labels: list, values: list, **kwargs):
  file_name = kwargs.get('file_name', None)
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  if file_name:
    plt.savefig('./charts/%s.png' % file_name)
  else:
    rand = random.randrange(1, 100)
    plt.savefig('./charts/chart_%s.png' % rand)
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [23, 112, 32]
  # generate_barchart(labels, values)
  generate_piechart(labels, values)
