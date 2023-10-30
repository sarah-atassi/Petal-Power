import codecademylib3
import pandas as pd
#load data into inventory dataframe:
inventory = pd.read_csv('inventory.csv')
staten_island = inventory.head(10)
#print(staten_island)
product_request = staten_island['product_description']
print(product_request)

#what types of seeds are sold at the Brooklyn location?
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type']== 'seeds')]
print(seed_request)

#inventory:
inventory['in_stock'] = inventory['quantity'].apply(lambda x:
True
if x > 0
else False) 


#creat a column called total value which is the value of the current inventory:
inventory['total_value'] = inventory['price'] * inventory['quantity']


combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)
print(inventory)
