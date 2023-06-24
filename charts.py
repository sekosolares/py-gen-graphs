import matplotlib.pyplot as plt
import random

def generate_barchart(labels: list, values: list):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  rand = random.randrange(1, 100)
  plt.savefig('./charts/chart_%s.png' % rand)
  plt.close()

def generate_piechart(labels: list, values: list):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  rand = random.randrange(1, 100)
  plt.savefig('./charts/chart_%s.png' % rand)
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [23, 112, 32]
  # generate_barchart(labels, values)
  generate_piechart(labels, values)
