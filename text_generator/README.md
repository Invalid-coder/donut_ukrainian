# text generator

## Step 1

pip install Faker

## Step 2

Generate text with addresses

python address_generator.py --templates_path templates.xlsx --result_path result --random_seed 0 --samples_amount 10

## Step 3

Generate text with addresses, organization names and full names

python text_generator.py --templates_path templates.xlsx --result_path result --random_seed 0 --samples_amount 10

- templates_path - path to the templates file
- result_path - path to the result folder
- random_seed - random seed value
- samples_amount - amount of samples
