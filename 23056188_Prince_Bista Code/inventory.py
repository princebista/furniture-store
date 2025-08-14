import csv

FILE_PATH = 'stocks.txt'  # Define the file path for the inventory file

def read_inventory():
    inventory = {} # Initialize an empty dictionary to store inventory data
    with open(FILE_PATH, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 5:
                id_, manufacturer, product_name, quantity, price = row

                
                 # Store the inventory data in the dictionary with ID as the key
                inventory[id_] = { 
                    'manufacturer': manufacturer,
                    'product_name': product_name,
                    'quantity': int(quantity),
                    'price': float(price.replace('$', '').replace(',', '')) # Convert price to float after removing currency symbol
                }
    return inventory

def write_inventory(inventory):
    with open(FILE_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        for id_, details in inventory.items():
            writer.writerow([
                id_,
                details['manufacturer'],
                details['product_name'],
                details['quantity'],
                "$" + str(details['price'])
            ])
