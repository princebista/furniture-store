from datetime import datetime
from inventory import read_inventory


# Function to generate a purchase invoice
  while True:
                pass 
            
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') # Define the filename with a timestamp
    filename = "purchase_invoice_" + timestamp + ".txt"
    total_amount = 0
    
    with open(filename, 'w') as file:
        file.write("Purchase Invoice\n")
        file.write("Employee: " + employee_name + "\n")
        file.write("Date and Time: " + str(datetime.now()) + "\n")
        file.write("ID          Manufacturer         Product Name          Quantity    Price      Total\n")
        file.write("="*100 + "\n")
        
        inventory = read_inventory()
        for id_, quantity in purchases.items():
            item = inventory[id_]
            total_price = item['price'] * quantity
            total_amount += total_price
            
            file.write(id_ + " " + item['manufacturer'] + " " + item['product_name'] + " " + str(quantity) + " $" + str(item['price']) + " $" + str(total_price) + "\n")
        

         # Calculate VAT
        vat_amount = total_amount * 0.13  
        total_amount_with_vat = total_amount + vat_amount  
        
        file.write("="*100 + "\n")
        file.write("Subtotal: $" + str(total_amount) + "\n")
        file.write("VAT (13%): $" + str(vat_amount) + "\n")
        file.write("Total Amount (with VAT): $" + str(total_amount_with_vat) + "\n")
    

    print("Purchase invoice generated: " + filename)
