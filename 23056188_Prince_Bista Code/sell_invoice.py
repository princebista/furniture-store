from datetime import datetime
from inventory import read_inventory

# Function to generate a sales invoice
def generate_sales_invoice(customer_name, purchases, shipping_cost):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = "sales_invoice_" + timestamp + ".txt"
    total_amount_before_vat = 0
    
    with open(filename, 'w') as file:
        file.write("Sales Invoice\n")
        file.write("Customer: " + customer_name + "\n")
        file.write("Date and Time: " + str(datetime.now()) + "\n")
        file.write("ID          Manufacturer         Product Name          Quantity    Price      Total\n")
        file.write("="*100 + "\n")
        
        inventory = read_inventory()
        for id_, quantity in purchases.items():
            item = inventory[id_]
            total_price = item['price'] * quantity
            total_amount_before_vat += total_price
            
            file.write(id_ + " " + item['manufacturer'] + " " + item['product_name'] + " " + str(quantity) + " $" + str(item['price']) + " $" + str(total_price) + "\n")
        
        vat_amount = total_amount_before_vat * 0.13
        total_amount_after_vat = total_amount_before_vat + vat_amount
        final_total_amount = total_amount_after_vat + shipping_cost

 # Write the subtotal, VAT, shipping cost, and final total amount in the invoice
        file.write("="*100 + "\n")
        file.write("Total Amount before VAT: $" + str(total_amount_before_vat) + "\n")
        file.write("VAT (13%): $" + str(vat_amount) + "\n")
        file.write("Shipping Cost: $" + str(shipping_cost) + "\n")
        file.write("Total Amount to be Paid: $" + str(final_total_amount) + "\n")
    
    print("Sales invoice generated: " + filename)
