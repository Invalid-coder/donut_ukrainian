import os
import argparse
import pandas as pd
from faker import Faker


def replace(substr, offset):
  replaced = substr
  boundaries = dict()

  for i in range(len(generators)):
    replacement, generated = replacements[i], generators[i]()
    if replacement in replaced:
      low = len(replaced.split(replacement)[0]) + offset
      generated = 'ТОВ "{}"'.format(generated) if replacement == "?org_name" else generated
      high = low + len(generated) - 1
      replaced = replaced.replace(replacement,generated)
      boundaries[replacement] = (low, high)

  return replaced, boundaries


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Text generator')
  parser.add_argument("--templates_path", help="Path to the templates")
  parser.add_argument("--result_path", help="Path to the result_folder")
  parser.add_argument("--random_seed", help="Random seed")
  parser.add_argument("--samples_amount", help="Amount of samples to generate")
  args = parser.parse_args()
  templates_path = args.templates_path
  result_path = args.result_path
  random_seed = args.random_seed
  samples_amount = args.samples_amount

  fake = Faker('uk_UA')
  Faker.seed()
  dataframe = pd.read_excel(templates_path, dtype=str)
  dataframe.fillna('', inplace=True)
  low = 0

  if not os.path.exists(result_path):
      os.makedirs(result_path)

  generators = [fake.name, fake.company, fake.address]
  replacements = ["?org_name", "?full_name", "?address"]
  
  with open(result_path + '/input.txt', 'w', encoding='utf-8') as x:
    with open(result_path + '/target.txt', 'w', encoding='utf-8') as y:
      for i in range(len(dataframe['Subject'])):
        for j in range(int(samples_amount)):
          sample = ''
          target = dict()
          low = 0
          for key in dataframe.keys():
            if not sample:
              sample, boundary = replace(dataframe[key][i], low)
              target.update(boundary)
            else:
              if dataframe[key][i]:
                replaced, boundary = replace(dataframe[key][i], low)
                sample = sample + " " + replaced
                target.update(boundary)
            low = len(sample) + 1
          sample += "."
          x.write(sample)
          x.write('\n')
          y.write(str(target))
          y.write('\n')
