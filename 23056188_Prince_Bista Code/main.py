from inventory import read_inventory, write_inventory
from purchase_invoice import generate_purchase_invoice
from sell_invoice import generate_sales_invoice

# Function to handle furniture ordering
def order_furniture():
    employee_name = input("Enter your name (employee): ")
    purchases = {}
    inventory = read_inventory()
    
    # Display available furniture with details
    print("Available furniture:")
    for id_, details in inventory.items():
        print("ID: {0} Manufacturer: {1} Product: {2} Price: ${3}".format(id_, details['manufacturer'], details['product_name'], details['price']))
    
     # Loop to allow multiple orders
    while True:
        id_ = input("Enter Furniture ID to order (or type 'done' to finish): ")
        if id_ == 'done':
            break
        if id_ not in inventory:
            print("Error: Furniture ID {0} not found.".format(id_))
            continue
        try:
            quantity = int(input("Enter quantity for Furniture ID {0}: ".format(id_)))
        except ValueError:
            print("Error: Please enter a valid number for quantity.")
            continue
        purchases[id_] = quantity
    
    generate_purchase_invoice(employee_name, purchases)
    

    # Update the inventory with new quantities
    for id_, quantity in purchases.items():
        inventory[id_]['quantity'] += quantity
    
    write_inventory(inventory)





# Function to handle furniture selling
def sell_furniture():
    customer_name = input("Enter customer name: ")
    purchases = {}
    inventory = read_inventory()
    
    print("Available furniture:")
    for id_, details in inventory.items():
        print("ID: {0} Manufacturer: {1} Product: {2} Price: ${3}".format(id_, details['manufacturer'], details['product_name'], details['price']))
    
    while True:
        id_ = input("Enter Furniture ID to sell (or type 'done' to finish): ")
        if id_ == 'done':
            break
        if id_ not in inventory:
            print("Error: Furniture ID {0} not found.".format(id_))
            continue
        try:
            quantity = int(input("Enter quantity for Furniture ID {0}: ".format(id_)))
        except ValueError:
            print("Error: Please enter a valid number for quantity.")
            continue
        if inventory[id_]['quantity'] < quantity:
            print("Error: Insufficient stock for Furniture ID {0}.".format(id_))
            continue
        purchases[id_] = quantity
    
    try:
        shipping_cost = float(input("Enter shipping cost: "))
    except ValueError:
        print("Error: Please enter a valid number for shipping cost.")
        return
    
    generate_sales_invoice(customer_name, purchases, shipping_cost)
    
    for id_, quantity in purchases.items():
        inventory[id_]['quantity'] -= quantity
    
    write_inventory(inventory)




# Main function to handle the user interface
if __name__ == "__main__":
    while True:
        print("\n1. Order Furniture")
        print("2. Sell Furniture")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            order_furniture()
        elif choice == '2':
            sell_furniture()
        elif choice == '3':
            print("Program terminated successfully.")  
            
            
            while True:
                pass 
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


