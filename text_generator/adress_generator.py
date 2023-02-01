import argparse
import pandas as pd
from faker import Faker


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
    dataframe = pd.read_excel(templates_path)

    with open('input.txt', 'w') as x:
        with open('target.txt', 'w') as y:
            for i in range(len(dataframe['input'])):
                for j in range(int(samples_amount)):
                    address = fake.address()
                    x.write(dataframe['input'][i].replace('?address', address))
                    x.write('\n')
                    y.write(dataframe['target'][i].replace('?address', address))
                    y.write('\n')
